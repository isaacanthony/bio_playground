"""Logging wrapper"""
import logging
import sys


def getLogger(name: str) -> logging.Logger:
    """Logging wrapper"""
    stdout = logging.StreamHandler(sys.stdout)
    stdout.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    stdout.setLevel(logging.INFO)

    logger = logging.getLogger(name)
    logger.addHandler(stdout)
    logger.setLevel(logging.INFO)

    return logger
