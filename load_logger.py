import logging


def load_logger() -> logging.Logger:
    """Return a logger instance."""

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("status.log")
    stream_handler = logging.StreamHandler()

    file_handler.setLevel(logging.INFO)
    stream_handler.setLevel(logging.WARNING)

    log_format = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")

    file_handler.setFormatter(log_format)
    stream_handler.setFormatter(log_format)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
