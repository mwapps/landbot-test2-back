import logging

from app.config import Config


def init_logging():
    config = Config()
    level_str = config.get("LOGGING_LEVEL", "INFO").upper()
    level = getattr(logging, level_str, logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
