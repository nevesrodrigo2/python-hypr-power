# button_module.py
from gi.repository import Gtk, GdkPixbuf

class PowerButton(Gtk.Button):
    def __init__(self, label_text, icon_path):
        super().__init__()

        # Box to hold image and label
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)
        box.get_style_context().add_class("power-button-box")
        self.set_relief(Gtk.ReliefStyle.NONE)  # Removes default button relief/padding
        self.set_border_width(0) 
        self.add(box)

        # Image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(icon_path, width=100, height=100, preserve_aspect_ratio=True)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.get_style_context().add_class("power-button-icon")
        box.pack_start(image, False, False, 0)

        # Label
        label = Gtk.Label(label=label_text)
        label.get_style_context().add_class("power-button-label")
        box.pack_start(label, False, False, 0)

        # Add CSS class to the button
        self.get_style_context().add_class("power-button")