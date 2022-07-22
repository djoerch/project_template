import logging
import coloredlogs

from argparse import ArgumentParser
from typing import Dict, Union

__VERBOSITY_GRANULARITY__ = 2

LOG_FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# define custom log levels
DEBUG = logging.DEBUG
DEBUG2 = DEBUG - 2
DEBUG4 = DEBUG - 4
DEBUG6 = DEBUG - 6
# add levels to the 'DEBUG' group (i.e. same coloring)
for lvl_value in [DEBUG2, DEBUG4, DEBUG6]:
    logging.addLevelName(lvl_value, "DEBUG")


def setup_logging(level: Union[str, int] = "DEBUG"):
    coloredlogs.install(level=level, fmt=LOG_FMT)


def get_logger(name: str = "", level: Union[str, int] = None) -> logging.Logger:
    """Get a logger and setup colored logging if level is provided."""

    if level is not None:
        setup_logging(level=level)

    return logging.getLogger(name)


def get_filehandler(path_to_file: str):
    """Get a logging file handler with standard settings."""
    fh = logging.FileHandler(path_to_file, mode="a")
    fh.setFormatter(logging.Formatter(fmt=LOG_FMT))
    return fh


def add_verbosity_options_to_argparser(p: ArgumentParser):
    gp = p.add_mutually_exclusive_group(required=False)
    gp.add_argument(
        "-v",
        "--verbose",
        required=False,
        action="count",
        help="Enable verbose output in terminal. "
        "Add multiple times to increase verbosity.",
    )
    gp.add_argument(
        "-q",
        "--silent",
        required=False,
        action="count",
        help="Suppress most log outputs in terminal.",
    )


def log_lvl_from_verbosity_args(args: Dict) -> int:
    if args["verbose"]:
        return logging.DEBUG - __VERBOSITY_GRANULARITY__ * (args["verbose"] - 1)
    elif args["silent"]:
        return logging.WARN
    else:
        return logging.INFO
