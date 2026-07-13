from dataclasses import dataclass


@dataclass
class JadwalItem:
    tahun_ajaran_id: int
    guru_id: int
    kelas_id: int
    mapel_id: int
    hari: str
    jam_mulai: str
    jam_selesai: str
    created_at: str = ""
    updated_at: str = ""

    def to_tuple(self) -> tuple:
        return (
            self.tahun_ajaran_id,
            self.guru_id,
            self.kelas_id,
            self.mapel_id,
            self.hari,
            self.jam_mulai,
            self.jam_selesai,
            self.created_at,
            self.updated_at,
        )


@dataclass
class ParseError:
    hari: str
    kelas: str
    waktu: str
    cell_value: str
    reason: str

    def __str__(self) -> str:
        return f"[{self.hari}] {self.kelas} @ {self.waktu}: '{self.cell_value}' -> {self.reason}"