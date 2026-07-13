"""
SIJUMA Jadwal Converter
Entry point for the application.
"""

import logging
import sys
from pathlib import Path

import config


def setup_logging() -> None:
    config.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = config.LOGS_DIR / "error_log.txt"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(str(log_file), encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("SIJUMA Jadwal Converter starting...")

    try:
        from gui import launch_gui
        launch_gui()
    except ImportError as e:
        logger.error("Failed to import GUI module: %s", e)
        logger.error("Make sure customtkinter is installed: pip install customtkinter")
        sys.exit(1)
    except Exception as e:
        logger.exception("Application error: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()