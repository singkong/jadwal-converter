import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
LOGS_DIR = BASE_DIR / "logs"

JADWAL_EXCEL = INPUT_DIR / "Jadwal.xlsx"
GURU_SQL = INPUT_DIR / "gurus.sql"
KELAS_SQL = INPUT_DIR / "kelas.sql"
MAPEL_SQL = INPUT_DIR / "mapels.sql"
TAHUN_AJARAN_SQL = INPUT_DIR / "tahun_ajarans.sql"

OUTPUT_SQL = OUTPUT_DIR / "jadwal_import.sql"
OUTPUT_EXCEL = OUTPUT_DIR / "jadwal_import.xlsx"
OUTPUT_CSV = OUTPUT_DIR / "jadwal_import.csv"
ERROR_LOG = LOGS_DIR / "error_log.txt"

CLASS_ORDER = [
    "X ATPH", "X MP 1", "X MP 2", "X TKJ 1", "X TKJ 2",
    "X TSM 1", "X TSM 2",
    "XI ATPH", "XI MP", "XI TKJ 1", "XI TKJ 2",
    "XI TSM 1", "XI TSM 2",
    "XII ATPH", "XII MP", "XII TKJ 1", "XII TKJ 2",
    "XII TSM 1", "XII TSM 2",
]

DAYS = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

DAY_BLOCKS = [
    {"hari": "Senin", "start_row": 6, "end_row": 16, "jam_col": 3, "start_col": 4},
    {"hari": "Selasa", "start_row": 6, "end_row": 16, "jam_col": 25, "start_col": 26},
    {"hari": "Rabu", "start_row": 6, "end_row": 16, "jam_col": 46, "start_col": 47},
    {"hari": "Kamis", "start_row": 6, "end_row": 16, "jam_col": 67, "start_col": 68},
    {"hari": "Jumat", "start_row": 6, "end_row": 16, "jam_col": 88, "start_col": 89},
]

IGNORE_KEYWORDS = [
    "ISTIRAHAT", "UPACARA", "LITERASI", "SENAM",
    "EKSTRAKURIKULER", "EKTRAKURIKULER",
]

NUM_CLASSES = 19

COLUMNS = [
    "tahun_ajaran_id", "guru_id", "kelas_id", "mapel_id",
    "hari", "jam_mulai", "jam_selesai",
    "created_at", "updated_at",
]

for d in [INPUT_DIR, OUTPUT_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)