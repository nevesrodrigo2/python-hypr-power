#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from python_hypr_power.power_menu import PowerMenu
from python_hypr_power.settings import Settings
from python_hypr_power.logger import logger

import python_hypr_power.config as config

def main():
    settings = Settings()
    settings.set_font(config.FONT_TOTAL)

    logger.info("Application started")  

    window = PowerMenu()
    Gtk.main()

if __name__ == '__main__':
    main()
