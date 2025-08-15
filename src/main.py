#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from src.power_menu import PowerMenu

window = PowerMenu()
window.show_all()
window.connect('destroy', Gtk.main_quit)
Gtk.main()
