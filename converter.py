import logging
from datetime import datetime
from typing import Any

import config
from excel_reader import ExcelReader
from mapper import Mapper
from models import JadwalItem, ParseError

logger = logging.getLogger(__name__)


class Converter:
    def __init__(self, mapper: Mapper, tahun_ajaran_id: int) -> None:
        self.mapper = mapper
        self.tahun_ajaran_id = tahun_ajaran_id
        self.items: list[JadwalItem] = []
        self.errors: list[ParseError] = []

    def convert(self, excel_path: str) -> tuple[list[JadwalItem], list[ParseError]]:
        self.items = []
        self.errors = []
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        reader = ExcelReader(excel_path)
        try:
            for block in config.DAY_BLOCKS:
                self._process_block(reader, block, now_str)
        finally:
            reader.close()

        logger.info(
            "Conversion complete: %d items, %d errors",
            len(self.items),
            len(self.errors),
        )
        return self.items, self.errors

    def _process_block(
        self, reader: ExcelReader, block: dict[str, Any], now_str: str
    ) -> None:
        hari = block["hari"]
        start_row = block["start_row"]
        end_row = block["end_row"]
        jam_col = block["jam_col"]
        start_col = block["start_col"]

        for row in range(start_row, end_row + 1):
            jam_raw = reader.cell_value(row, jam_col)
            jam_parsed = ExcelReader.parse_jam(jam_raw)
            if jam_parsed is None:
                continue
            jam_mulai, jam_selesai = jam_parsed

            for class_idx in range(config.NUM_CLASSES):
                col = start_col + class_idx
                cell_raw = reader.cell_value(row, col)
                parsed = ExcelReader.parse_cell(cell_raw, self.errors)
                if parsed is None:
                    continue
                teacher_code, subject_code = parsed

                if class_idx >= len(config.CLASS_ORDER):
                    continue
                kelas_name = config.CLASS_ORDER[class_idx]

                err_info = ParseError(
                    hari=hari,
                    kelas=kelas_name,
                    waktu=f"{jam_mulai}-{jam_selesai}",
                    cell_value=str(cell_raw),
                    reason="",
                )

                guru_id = self.mapper.get_guru_id(str(teacher_code), err_info)
                mapel_id = self.mapper.get_mapel_id(subject_code, err_info)
                kelas_id = self.mapper.get_kelas_id(kelas_name, err_info)

                if guru_id is None:
                    err_info.reason = f"Guru code '{teacher_code}' not found in database"
                    self.errors.append(err_info)
                    continue
                if mapel_id is None:
                    err_info.reason = f"Mapel code '{subject_code}' not found in database"
                    self.errors.append(err_info)
                    continue
                if kelas_id is None:
                    err_info.reason = f"Kelas '{kelas_name}' not found in database"
                    self.errors.append(err_info)
                    continue

                item = JadwalItem(
                    tahun_ajaran_id=self.tahun_ajaran_id,
                    guru_id=guru_id,
                    kelas_id=kelas_id,
                    mapel_id=mapel_id,
                    hari=hari,
                    jam_mulai=jam_mulai,
                    jam_selesai=jam_selesai,
                    created_at=now_str,
                    updated_at=now_str,
                )
                self.items.append(item)