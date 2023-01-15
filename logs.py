import logging


def logs() -> logging.Logger:
    # Generating a logger and creating a template for it
    logger = logging.getLogger(__name__)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '########\n%(levelname)s - %(asctime)s - %(message)s'
    )

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
