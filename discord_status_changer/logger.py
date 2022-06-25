import datetime
import logging
import os
import zlib
from logging.handlers import RotatingFileHandler

reset = "\x1b[0m"
FORMATS = {
    logging.DEBUG: "\u001b[38;5;247m",
    logging.WARNING: "\u001b[38;5;11m",
    logging.ERROR: "\u001b[38;5;196m",
    logging.CRITICAL: "\u001b[38;5;52m",
    logging.INFO: "\u001b[38;5;46m",
}

LOG_FOLDER = f"/var/tmp/logs"
LOG_FILE: str = f"{LOG_FOLDER}/discord {datetime.datetime.now()}.log"

COLORS = [
    46,
    27,
    44,
    93,
    118,
    128,
    123,
    131,
    134,
    30,
    47,
    64,
    68,
    138,
    141,
    147,
    151,
    155,
    165,
    175,
    183,
    192,
    201,
    210,
]


def paint_level(level: int, text: str) -> str:
    return f"{FORMATS[level]}{text}{reset}"


def paint_name(text: str) -> str:
    color = (
        "\u001b[38;5;" + str(COLORS[zlib.adler32(text.encode()) % len(COLORS)]) + "m"
    )
    return f"{color}{text}{reset}"


class LoggerFormatter(logging.Formatter):
    name_just = 20
    level_just = 40

    def __init__(
        self,
        splitter: str,
        show_func: bool = False,
        emphasize_from: int = logging.ERROR,
    ):
        """
        Args:
            splitter: string used to split different part of the log text
                     should be a single character
            show_func: wether or not show function_name in log text
                       its false by default meaning it only shows line number
            emphasize_from: make whole log line colorized should the log_level be greater
                            than `emphasize_from`
        """
        super().__init__()
        self.splitter = splitter
        self.show_func = show_func
        self.emphasize_from = emphasize_from

    def format(self, record: logging.LogRecord) -> str:
        time = self.formatTime(record, self.datefmt)
        split_3 = self.splitter * 3
        log_text = (
            f"{split_3}[{time}]{split_3}[{record.levelname}]".ljust(
                self.level_just, self.splitter
            )
            + f"{split_3}[{record.name}]{split_3}".ljust(self.name_just, self.splitter)
            + f" {record.getMessage()} :: ({record.filename}:"
            + (f"{record.lineno}", record.funcName)[self.show_func]
            + ")"
        )
        if record.levelno >= self.emphasize_from:
            return paint_level(record.levelno, log_text)
        return log_text.replace(
            record.levelname, paint_level(record.levelno, record.levelname)
        ).replace(record.name, paint_name(record.name))


def get_logger(
    name: str,
    level: int = logging.NOTSET,
    split: str = "=",
    show_func: bool = False,
    emphasize_from: int = logging.ERROR,
) -> logging.Logger:
    lev_tmp = os.getenv("GAY_LEVEL")
    if level is logging.NOTSET:
        level = (lev_tmp, logging.INFO)[lev_tmp is None]  # type: ignore
    stdout_h = logging.StreamHandler()
    stdout_h.setLevel(level)
    stdout_h.setFormatter(LoggerFormatter(split, show_func, emphasize_from))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stdout_h)

    os.makedirs(LOG_FOLDER, exist_ok=True)
    logger.addHandler(
        RotatingFileHandler(LOG_FILE, maxBytes=50 * 1024 * 1024, backupCount=5)
    )

    return logger
