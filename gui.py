import logging
import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox
from typing import Any

import customtkinter as ctk

import config
from converter import Converter
from excel_reader import ExcelReader
from exporter import Exporter
from mapper import Mapper
from sql_reader import SQLReader

logger = logging.getLogger(__name__)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class JadwalConverterGUI(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("SIJUMA Jadwal Converter")
        self.geometry("1000x750")
        self.minsize(800, 600)

        self.items: list[Any] = []
        self.errors: list[Any] = []

        self._setup_paths()
        self._build_ui()

        self.after(100, self._auto_load_defaults)

    def _setup_paths(self) -> None:
        self.excel_path = ctk.StringVar(value=str(config.JADWAL_EXCEL))
        self.guru_path = ctk.StringVar(value=str(config.GURU_SQL))
        self.kelas_path = ctk.StringVar(value=str(config.KELAS_SQL))
        self.mapel_path = ctk.StringVar(value=str(config.MAPEL_SQL))
        self.tahun_ajaran_path = ctk.StringVar(value=str(config.TAHUN_AJARAN_SQL))
        self.tahun_ajaran_id = ctk.StringVar(value="")
        self.tahun_ajaran_label = ctk.StringVar(value="")

    def _build_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self._build_title()
        self._build_file_section()
        self._build_tahun_ajaran_section()
        self._build_convert_section()
        self._build_log_section()
        self._build_export_section()

    def _build_title(self) -> None:
        title_frame = ctk.CTkFrame(self)
        title_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
        title_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            title_frame,
            text="SIJUMA Jadwal Converter",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        title_label.grid(row=0, column=0, pady=10)

    def _build_file_section(self) -> None:
        file_frame = ctk.CTkFrame(self)
        file_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        file_frame.grid_columnconfigure(1, weight=1)

        row = 0
        self._add_file_row(file_frame, row, "File Jadwal Excel", self.excel_path, self._browse_excel)
        row += 1
        self._add_file_row(file_frame, row, "File Guru SQL", self.guru_path, self._browse_guru)
        row += 1
        self._add_file_row(file_frame, row, "File Kelas SQL", self.kelas_path, self._browse_kelas)
        row += 1
        self._add_file_row(file_frame, row, "File Mapel SQL", self.mapel_path, self._browse_mapel)
        row += 1
        self._add_file_row(file_frame, row, "File Tahun Ajaran SQL", self.tahun_ajaran_path, self._browse_tahun_ajaran)

    def _add_file_row(
        self,
        parent: ctk.CTkFrame,
        row: int,
        label: str,
        var: ctk.StringVar,
        browse_cmd: Any,
    ) -> None:
        lbl = ctk.CTkLabel(parent, text=label, width=160, anchor="w")
        lbl.grid(row=row, column=0, padx=(10, 5), pady=3, sticky="w")

        entry = ctk.CTkEntry(parent, textvariable=var)
        entry.grid(row=row, column=1, padx=5, pady=3, sticky="ew")

        btn = ctk.CTkButton(parent, text="Browse", width=80, command=browse_cmd)
        btn.grid(row=row, column=2, padx=(5, 10), pady=3)

        open_btn = ctk.CTkButton(parent, text="Open", width=60, command=lambda p=var.get(): self._open_folder(p))
        open_btn.grid(row=row, column=3, padx=(0, 10), pady=3)

    def _build_tahun_ajaran_section(self) -> None:
        ta_frame = ctk.CTkFrame(self)
        ta_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        ta_frame.grid_columnconfigure(1, weight=1)

        lbl = ctk.CTkLabel(ta_frame, text="Tahun Ajaran ID", width=160, anchor="w")
        lbl.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        self.ta_entry = ctk.CTkEntry(ta_frame, textvariable=self.tahun_ajaran_id)
        self.ta_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.ta_load_btn = ctk.CTkButton(
            ta_frame, text="Load from SQL", command=self._load_tahun_ajaran_from_sql
        )
        self.ta_load_btn.grid(row=0, column=2, padx=5, pady=5)

        self.ta_info_label = ctk.CTkLabel(ta_frame, textvariable=self.tahun_ajaran_label, text_color="gray")
        self.ta_info_label.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    def _build_convert_section(self) -> None:
        convert_frame = ctk.CTkFrame(self)
        convert_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        convert_frame.grid_columnconfigure(0, weight=1)

        btn_frame = ctk.CTkFrame(convert_frame, fg_color="transparent")
        btn_frame.grid(row=0, column=0, pady=5)

        self.convert_btn = ctk.CTkButton(
            btn_frame,
            text="Convert",
            width=200,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self._start_convert,
        )
        self.convert_btn.pack(side="left", padx=5)

        self.progress = ctk.CTkProgressBar(convert_frame, mode="indeterminate")
        self.progress.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.progress.set(0)

        self.status_var = ctk.StringVar(value="Ready")
        self.status_label = ctk.CTkLabel(convert_frame, textvariable=self.status_var)
        self.status_label.grid(row=2, column=0, padx=10, pady=(0, 5), sticky="w")

    def _build_log_section(self) -> None:
        log_frame = ctk.CTkFrame(self)
        log_frame.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
        log_frame.grid_columnconfigure(0, weight=1)
        log_frame.grid_rowconfigure(1, weight=1)

        log_header = ctk.CTkLabel(
            log_frame, text="Log Output", font=ctk.CTkFont(weight="bold")
        )
        log_header.grid(row=0, column=0, padx=10, pady=(5, 0), sticky="w")

        self.log_text = ctk.CTkTextbox(log_frame, font=ctk.CTkFont(size=11, family="Consolas"))
        self.log_text.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        log_btn_frame = ctk.CTkFrame(log_frame, fg_color="transparent")
        log_btn_frame.grid(row=2, column=0, pady=(0, 5))

        self.clear_log_btn = ctk.CTkButton(
            log_btn_frame, text="Clear Log", width=100, command=self._clear_log
        )
        self.clear_log_btn.pack(side="left", padx=5)

    def _build_export_section(self) -> None:
        export_frame = ctk.CTkFrame(self)
        export_frame.grid(row=5, column=0, padx=10, pady=(5, 10), sticky="ew")
        export_frame.grid_columnconfigure(0, weight=1)

        btn_frame = ctk.CTkFrame(export_frame, fg_color="transparent")
        btn_frame.grid(row=0, column=0, pady=5)

        self.export_sql_btn = ctk.CTkButton(
            btn_frame, text="Export SQL", width=130, state="disabled", command=self._export_sql
        )
        self.export_sql_btn.pack(side="left", padx=5)

        self.export_excel_btn = ctk.CTkButton(
            btn_frame, text="Export Excel", width=130, state="disabled", command=self._export_excel
        )
        self.export_excel_btn.pack(side="left", padx=5)

        self.export_csv_btn = ctk.CTkButton(
            btn_frame, text="Export CSV", width=130, state="disabled", command=self._export_csv
        )
        self.export_csv_btn.pack(side="left", padx=5)

        self.status_bar = ctk.CTkLabel(
            export_frame, text="", anchor="w", fg_color="transparent"
        )
        self.status_bar.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")

    def _open_folder(self, path: str) -> None:
        try:
            folder = Path(path).parent
            if folder.exists():
                import subprocess
                subprocess.Popen(["explorer", str(folder.resolve())])
        except Exception:
            pass

    def _browse_excel(self) -> None:
        path = filedialog.askopenfilename(
            title="Select Jadwal Excel",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")],
            initialdir=str(config.INPUT_DIR),
        )
        if path:
            self.excel_path.set(path)

    def _browse_guru(self) -> None:
        path = filedialog.askopenfilename(
            title="Select Guru SQL",
            filetypes=[("SQL files", "*.sql"), ("All files", "*.*")],
            initialdir=str(config.INPUT_DIR),
        )
        if path:
            self.guru_path.set(path)

    def _browse_kelas(self) -> None:
        path = filedialog.askopenfilename(
            title="Select Kelas SQL",
            filetypes=[("SQL files", "*.sql"), ("All files", "*.*")],
            initialdir=str(config.INPUT_DIR),
        )
        if path:
            self.kelas_path.set(path)

    def _browse_mapel(self) -> None:
        path = filedialog.askopenfilename(
            title="Select Mapel SQL",
            filetypes=[("SQL files", "*.sql"), ("All files", "*.*")],
            initialdir=str(config.INPUT_DIR),
        )
        if path:
            self.mapel_path.set(path)

    def _browse_tahun_ajaran(self) -> None:
        path = filedialog.askopenfilename(
            title="Select Tahun Ajaran SQL",
            filetypes=[("SQL files", "*.sql"), ("All files", "*.*")],
            initialdir=str(config.INPUT_DIR),
        )
        if path:
            self.tahun_ajaran_path.set(path)

    def _load_tahun_ajaran_from_sql(self) -> None:
        path = self.tahun_ajaran_path.get()
        if not path or not Path(path).exists():
            messagebox.showerror("Error", "Tahun Ajaran SQL file not found")
            return
        try:
            reader = SQLReader(path)
            ta_map = reader.to_tahun_ajaran_dict()
            if not ta_map:
                messagebox.showwarning("Warning", "No tahun ajaran found in SQL file")
                return

            ids = sorted(set(v for v in ta_map.values()))

            if len(ids) == 1:
                self.tahun_ajaran_id.set(str(ids[0]))
                self.tahun_ajaran_label.set("(loaded from SQL)")
                self._log(f"Tahun Ajaran ID: {ids[0]} (loaded from SQL)")
            else:
                choice = self._select_tahun_ajaran(ids, ta_map)
                if choice is not None:
                    self.tahun_ajaran_id.set(str(choice))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tahun ajaran: {e}")

    def _select_tahun_ajaran(self, ids: list[int], ta_map: dict[str, int]) -> int | None:
        dialog = ctk.CTkInputDialog(
            title="Select Tahun Ajaran",
            text=f"Available IDs: {', '.join(str(i) for i in ids)}\nEnter Tahun Ajaran ID:",
        )
        result = dialog.get_input()
        if result:
            try:
                val = int(result.strip())
                if val in ids:
                    return val
                messagebox.showwarning("Warning", f"ID {val} not found in available IDs")
            except ValueError:
                messagebox.showerror("Error", "Invalid ID")
        return None

    def _auto_load_defaults(self) -> None:
        if Path(self.guru_path.get()).exists():
            self._log(f"Guru SQL: {self.guru_path.get()}")
        if Path(self.kelas_path.get()).exists():
            self._log(f"Kelas SQL: {self.kelas_path.get()}")
        if Path(self.mapel_path.get()).exists():
            self._log(f"Mapel SQL: {self.mapel_path.get()}")
        if Path(self.tahun_ajaran_path.get()).exists():
            self._load_tahun_ajaran_from_sql()
        if Path(self.excel_path.get()).exists():
            info = self._get_excel_info()
            if info:
                self._log(f"Excel: {info['sheet']} ({info['rows']} rows x {info['cols']} cols)")

    def _get_excel_info(self) -> dict[str, Any] | None:
        try:
            reader = ExcelReader(self.excel_path.get())
            info = reader.get_info()
            reader.close()
            return info
        except Exception as e:
            self._log(f"Error reading Excel: {e}")
            return None

    def _start_convert(self) -> None:
        if not self._validate_paths():
            return

        ta_id_str = self.tahun_ajaran_id.get().strip()
        if not ta_id_str:
            messagebox.showerror("Error", "Tahun Ajaran ID is required")
            return
        try:
            tahun_ajaran_id = int(ta_id_str)
        except ValueError:
            messagebox.showerror("Error", "Tahun Ajaran ID must be a number")
            return

        self._set_ui_state(False)
        self.progress.start()
        self._log("=" * 50)
        self._log("Conversion started...")

        thread = threading.Thread(
            target=self._run_conversion,
            args=(tahun_ajaran_id,),
            daemon=True,
        )
        thread.start()

    def _run_conversion(self, tahun_ajaran_id: int) -> None:
        try:
            self._log("Loading SQL data...")
            guru_map = SQLReader(self.guru_path.get()).to_guru_dict()
            kelas_map = SQLReader(self.kelas_path.get()).to_kelas_dict()
            mapel_map = SQLReader(self.mapel_path.get()).to_mapel_dict()

            self._log(f"  Guru mappings: {len(guru_map)}")
            self._log(f"  Kelas mappings: {len(kelas_map)}")
            self._log(f"  Mapel mappings: {len(mapel_map)}")

            mapper = Mapper(guru_map, kelas_map, mapel_map, {})

            self._log("Reading Excel and converting...")
            converter = Converter(mapper, tahun_ajaran_id)
            self.items, self.errors = converter.convert(self.excel_path.get())

            self.after(0, self._on_conversion_done)
        except Exception as e:
            logger.exception("Conversion failed")
            self.after(0, lambda: self._on_conversion_error(str(e)))

    def _on_conversion_done(self) -> None:
        self.progress.stop()
        self.progress.set(1)
        self._set_ui_state(True)

        self._log(f"Conversion complete!")
        self._log(f"  Total items: {len(self.items)}")
        self._log(f"  Total errors: {len(self.errors)}")

        if self.errors:
            self._log(f"\nErrors ({len(self.errors)}):")
            for err in self.errors:
                self._log(f"  {err}")

        self.export_sql_btn.configure(state="normal")
        self.export_excel_btn.configure(state="normal")
        self.export_csv_btn.configure(state="normal")

        self.status_var.set(f"Done: {len(self.items)} items, {len(self.errors)} errors")

    def _on_conversion_error(self, error_msg: str) -> None:
        self.progress.stop()
        self.progress.set(0)
        self._set_ui_state(True)
        self._log(f"ERROR: {error_msg}")
        self.status_var.set("Conversion failed")
        messagebox.showerror("Conversion Failed", error_msg)

    def _validate_paths(self) -> bool:
        paths = [
            ("Excel", self.excel_path.get()),
            ("Guru SQL", self.guru_path.get()),
            ("Kelas SQL", self.kelas_path.get()),
            ("Mapel SQL", self.mapel_path.get()),
        ]
        for name, path in paths:
            if not path or not Path(path).exists():
                messagebox.showerror("Error", f"{name} file not found: {path}")
                return False
        return True

    def _set_ui_state(self, enabled: bool) -> None:
        state = "normal" if enabled else "disabled"
        self.convert_btn.configure(state=state)
        self.ta_load_btn.configure(state=state)
        self.ta_entry.configure(state=state)
        for child in self.winfo_children():
            if isinstance(child, ctk.CTkFrame):
                for sub in child.winfo_children():
                    if isinstance(sub, ctk.CTkButton) and sub != self.convert_btn:
                        if sub.cget("text") in ("Export SQL", "Export Excel", "Export CSV"):
                            continue
                        if enabled or sub.cget("text") in ("Browse", "Open", "Clear Log"):
                            continue
                        try:
                            sub.configure(state="normal" if enabled else "disabled")
                        except Exception:
                            pass

    def _export_sql(self) -> None:
        if not self.items:
            return
        try:
            exporter = Exporter()
            exporter.export_sql(self.items, config.OUTPUT_SQL)
            self._log(f"SQL exported to {config.OUTPUT_SQL}")
            self.status_var.set(f"SQL exported: {config.OUTPUT_SQL}")
            messagebox.showinfo("Success", f"SQL exported to\n{config.OUTPUT_SQL}")
        except Exception as e:
            self._log(f"Export SQL failed: {e}")
            messagebox.showerror("Error", f"Export SQL failed: {e}")

    def _export_excel(self) -> None:
        if not self.items:
            return
        try:
            exporter = Exporter()
            exporter.export_excel(self.items, config.OUTPUT_EXCEL)
            self._log(f"Excel exported to {config.OUTPUT_EXCEL}")
            self.status_var.set(f"Excel exported: {config.OUTPUT_EXCEL}")
            messagebox.showinfo("Success", f"Excel exported to\n{config.OUTPUT_EXCEL}")
        except Exception as e:
            self._log(f"Export Excel failed: {e}")
            messagebox.showerror("Error", f"Export Excel failed: {e}")

    def _export_csv(self) -> None:
        if not self.items:
            return
        try:
            exporter = Exporter()
            exporter.export_csv(self.items, config.OUTPUT_CSV)
            self._log(f"CSV exported to {config.OUTPUT_CSV}")
            self.status_var.set(f"CSV exported: {config.OUTPUT_CSV}")
            messagebox.showinfo("Success", f"CSV exported to\n{config.OUTPUT_CSV}")
        except Exception as e:
            self._log(f"Export CSV failed: {e}")
            messagebox.showerror("Error", f"Export CSV failed: {e}")

    def _log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}] {message}"
        self.log_text.insert("end", line + "\n")
        self.log_text.see("end")

    def _clear_log(self) -> None:
        self.log_text.delete("1.0", "end")
        self._log("Log cleared")


def launch_gui() -> None:
    app = JadwalConverterGUI()
    app.mainloop()