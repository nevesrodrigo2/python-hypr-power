# SOURCE
# https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
# Modified it slightly to separate the color of each message section.
import logging
from python_hypr_power import config as config

class CustomFormatter(logging.Formatter):
    reset = "\x1b[0m"
    white = "\x1b[38;2;255;255;255m"

    # True color / 24-bit RGB codes for kitty
    grey = "\x1b[38;2;150;150;150m"
    yellow = "\x1b[38;2;255;255;0m"
    red = "\x1b[38;2;255;0;0m"
    bold_red = "\x1b[38;2;255;0;0;1m"  # red + bold
    green = "\x1b[38;2;0;255;0m"

    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    COLORS = {
        logging.DEBUG: green,
        logging.INFO: grey,
        logging.WARNING: yellow,
        logging.ERROR: red,
        logging.CRITICAL: bold_red
    }

    def format(self, record):

        color = self.COLORS.get(record.levelno, self.white)

        # make sure the message itself does not change color
        formatted = (
            f"{color}%(asctime)s - %(name)s - %(levelname)s{self.reset} - "
            f"{self.white}%(message)s{self.reset} "
            f"{color}(%(filename)s:%(lineno)d){self.reset}"
        )
        formatter = logging.Formatter(formatted)
        return formatter.format(record)

# Setup logger
logger = logging.getLogger(config.APP_NAME)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)