import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Settings():
    def __init__(self):
        self.settings = Gtk.Settings.get_default()

    def set_font(self, font_name):
        self.settings.set_property("gtk-font-name", font_name)
