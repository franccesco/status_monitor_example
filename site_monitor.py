import logging
import requests
from sys import argv
from sys import exit
from load_logger import load_logger


def main(domains_file: str) -> None:
    """Check for a number of HTTP codes and log them."""

    logger = load_logger()

    with open(domains_file, "r") as file:
        logger.info(f"Reading file: {domains_file}")
        domains = file.read().splitlines()

    for url in domains:
        logger.info(f"Sending get request to: {url}")

        try:
            req = requests.get(url)
        except Exception as e:
            logger.error(f"Destination unreachable for url: {url}")
            exit(1)
        else:
            if req.ok:
                logger.info(f"Status OK for url: {url}")
            else:
                logger.warning(f"Received status code: {req.status_code}")


if __name__ == "__main__":
    main(argv[1])
