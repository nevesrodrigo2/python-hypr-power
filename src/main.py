#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from src.power_menu import PowerMenu
from src.settings import Settings
import src.config as config

def main():
    settings = Settings()
    settings.set_font(config.FONT_TOTAL)

    window = PowerMenu()
    window.show_all()
    window.connect('destroy', Gtk.main_quit)
    Gtk.main()

if __name__ == '__main__':
    main()
