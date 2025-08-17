import subprocess
from cProfile import label
from gi.repository import Gtk, GdkPixbuf

class PowerButton(Gtk.Button):
    def __init__(self, label_text, icon_path, command):
        super().__init__()

        # css class
        self.get_style_context().add_class("power-button")

        self.label_text = label_text
        self.icon_path = icon_path
        self.command = command

        # Make the button focusable
        self.set_can_focus(True)
        self.set_focus_on_click(True)
        self.set_can_default(True)

        # button size
        self.set_size_request(400, 290)

        # Box to hold image and label
        self.load_box()

        # Image
        self.load_image()

        # Label
        self.load_label()

        self.show_all()

        # focus
        self.connect("enter-notify-event", lambda w, e: w.grab_focus())


    def load_box(self):
        """ Load the box container for the button. """
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        self.box.set_halign(Gtk.Align.CENTER)
        self.box.set_valign(Gtk.Align.CENTER)
        self.box.get_style_context().add_class("power-button-box")
        self.add(self.box)

    def load_image(self):
        """ Load the image for the button. """
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.icon_path, width=100, height=100, preserve_aspect_ratio=True)
        self.image = Gtk.Image.new_from_pixbuf(pixbuf)
        self.image.get_style_context().add_class("power-button-icon")
        self.box.pack_start(self.image, False, False, 0)

    def load_label(self):
        """ Load the label for the button. """
        self.label = Gtk.Label(label=self.label_text)
        self.label.get_style_context().add_class("power-button-label")
        self.box.pack_start(self.label, False, False, 0)
    
    