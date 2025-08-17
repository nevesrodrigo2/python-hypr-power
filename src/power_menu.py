import os
import subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GtkLayerShell, Gdk

from src.processes import processes
from src.power_button import PowerButton
import src.config as config

class PowerMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Power Menu")
        print(os.path.dirname(os.path.abspath(__file__)) )
        self.setup_css()
        self.set_default_size(1280, 720)
        self.setup_grid()
        self.set_can_focus(True)
        GtkLayerShell.init_for_window(self)
        GtkLayerShell.auto_exclusive_zone_enable(self)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.TOP, 0)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.BOTTOM, 0)

    def setup_grid(self):
        """ Setup the grid for the power buttons. """
        grid = Gtk.Grid()
        # grid.set_row_spacing(10)
        # grid.set_column_spacing(10)
        self.add(grid)

        row = 0
        col = 0

        for action, command in processes.items():
            icon_path = os.path.join(config.ICONS_DIR, f"{action}.png")
            power_button = PowerButton(label_text=action.capitalize(), icon_path=icon_path, command=command)
            grid.attach(power_button, col, row, 1, 1)

            col += 1
            if col > 2:  # Move to the next row after 3 buttons
                col = 0
                row += 1

    def setup_css(self):
        """ Setup the CSS for the window. """
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(os.path.join(config.STYLES_DIR, "styles.css")) 

        Gtk.StyleContext.add_provider_for_screen(
            self.get_screen(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER
        )