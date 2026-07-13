import logging
from typing import Any

from models import ParseError

logger = logging.getLogger(__name__)


class Mapper:
    def __init__(
        self,
        guru_map: dict[str, int],
        kelas_map: dict[str, int],
        mapel_map: dict[str, int],
        tahun_ajaran_map: dict[str, int],
    ) -> None:
        self.guru_map = guru_map
        self.kelas_map = kelas_map
        self.mapel_map = mapel_map
        self.tahun_ajaran_map = tahun_ajaran_map

    def get_guru_id(self, kode: str, error_info: ParseError | None = None) -> int | None:
        kode = str(kode).strip()
        if kode in self.guru_map:
            return self.guru_map[kode]
        logger.warning("Guru with code '%s' not found", kode)
        return None

    def get_kelas_id(self, nama: str, error_info: ParseError | None = None) -> int | None:
        nama = nama.strip()
        if nama in self.kelas_map:
            return self.kelas_map[nama]
        logger.warning("Kelas '%s' not found", nama)
        return None

    def get_mapel_id(self, kode: str, error_info: ParseError | None = None) -> int | None:
        kode = kode.strip().upper()
        if kode in self.mapel_map:
            return self.mapel_map[kode]
        logger.warning("Mapel with code '%s' not found", kode)
        return None

    def get_tahun_ajaran_id(self, key: str) -> int | None:
        key = key.strip()
        if key in self.tahun_ajaran_map:
            return self.tahun_ajaran_map[key]
        logger.warning("Tahun ajaran '%s' not found", key)
        return None

    def validate(self, errors: list[ParseError]) -> list[ParseError]:
        validation_errors: list[ParseError] = []
        for err in errors:
            validation_errors.append(err)
        return validation_errors