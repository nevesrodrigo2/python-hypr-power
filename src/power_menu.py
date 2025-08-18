import os
import subprocess
import sys
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1") 
from gi.repository import Gtk, GtkLayerShell, Gdk

from src.processes import processes
from src.power_button import PowerButton
import src.config as config

class PowerMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="PowerMenu")

        self.set_app_paintable(True)
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        # buttons 
        self.power_buttons = []
        self.current_button_index = -1

        # ---- LAYER SHELL  ----
        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.TOP)
        GtkLayerShell.set_keyboard_mode(self, GtkLayerShell.KeyboardMode.EXCLUSIVE)


        # Popup-like look/behavior
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_can_focus(True)

        # UI
        self.setup_css()
        self.setup_grid()

        # Events
        self.connect("key-press-event", self.on_escape)
        self.connect("destroy", Gtk.main_quit)

        # Show after all the above
        self.show_all()
    
    def on_escape(self, widget, event):
        """ Handle the escape key press event. """
        if event.keyval == Gdk.KEY_Escape:
            self.close()

    def setup_grid(self):
        """ Setup the grid for the power buttons. """
        self.grid = Gtk.Grid()
        self.add(self.grid)

        row = 0
        col = 0

        for action, command in processes.items():
            icon_path = os.path.join(config.ICONS_DIR, f"{action}.png")
            power_button = PowerButton(
                label_text=action.capitalize(), 
                icon_path=icon_path, 
                command=command
            )
            power_button.connect("clicked", self.on_button_clicked)

            self.grid.attach(power_button, col, row, 1, 1)
            self.power_buttons.append(power_button)

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

    def on_button_clicked(self, button):
        """ Handle button click events. """
        command = button.command
        self.hide()  # Hide immediately

        # run asynchronously
        subprocess.Popen(command, shell=True)
        self.destroy()
        sys.exit(0)