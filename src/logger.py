import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging():
    """Configura o sistema de logging para ficheiro e consola."""
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
        handlers=[
            RotatingFileHandler("logs/gestor.log", maxBytes=1_000_000, backupCount=3),
            logging.StreamHandler()
        ]
    )
