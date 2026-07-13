import re
import logging
from typing import Any

logger = logging.getLogger(__name__)


class SQLReader:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def load_raw(self) -> list[list[str]]:
        with open(self.filepath, "r", encoding="utf-8") as f:
            content = f.read()

        inserts = re.findall(
            r"INSERT\s+INTO.*?VALUES\s*(.*?);",
            content,
            re.IGNORECASE | re.DOTALL,
        )

        rows: list[list[str]] = []
        for block in inserts:
            values = re.findall(r"\((.*?)\)", block, re.DOTALL)
            for val in values:
                rows.append(self._split_values(val))
        return rows

    def _split_values(self, text: str) -> list[str]:
        result: list[str] = []
        current: list[str] = []
        in_quote = False

        for ch in text:
            if ch == "'":
                in_quote = not in_quote
                current.append(ch)
            elif ch == "," and not in_quote:
                result.append(self._clean("".join(current)))
                current = []
            else:
                current.append(ch)

        if current:
            result.append(self._clean("".join(current)))
        return result

    @staticmethod
    def _clean(val: str) -> str:
        val = val.strip().strip("'")
        if val == "NULL" or val == "":
            return ""
        return val

    def to_guru_dict(self) -> dict[str, int]:
        rows = self.load_raw()
        result: dict[str, int] = {}
        for row in rows:
            if not row:
                continue
            id_val = self._to_int(row[0])
            if id_val is not None:
                result[str(id_val)] = id_val
        logger.info("Loaded %d guru mappings", len(result))
        return result

    def to_mapel_dict(self) -> dict[str, int]:
        rows = self.load_raw()
        result: dict[str, int] = {}
        for row in rows:
            if len(row) < 2:
                continue
            id_val = self._to_int(row[0])
            kode = row[1].strip()
            if id_val is not None and kode:
                result[kode.upper()] = id_val
        logger.info("Loaded %d mapel mappings", len(result))
        return result

    def to_kelas_dict(self) -> dict[str, int]:
        rows = self.load_raw()
        result: dict[str, int] = {}
        for row in rows:
            if len(row) < 3:
                continue
            id_val = self._to_int(row[0])
            nama = row[2].strip()
            if id_val is not None and nama:
                result[nama] = id_val
        logger.info("Loaded %d kelas mappings", len(result))
        return result

    def to_tahun_ajaran_dict(self) -> dict[str, int]:
        rows = self.load_raw()
        result: dict[str, int] = {}
        for row in rows:
            if not row:
                continue
            id_val = self._to_int(row[0])
            if id_val is not None:
                result[str(id_val)] = id_val
                label = row[1].strip() if len(row) > 1 else ""
                if label:
                    result[label] = id_val
        logger.info("Loaded %d tahun_ajaran mappings", len(result))
        return result

    @staticmethod
    def _to_int(val: str) -> int | None:
        try:
            return int(val.strip().strip("'").strip('"'))
        except (ValueError, AttributeError):
            return None