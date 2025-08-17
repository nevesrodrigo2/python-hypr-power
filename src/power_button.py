import subprocess
from cProfile import label
from gi.repository import Gtk, GdkPixbuf

class PowerButton(Gtk.Button):
    def __init__(self, label_text, icon_path, command):
        super().__init__()
        self.label_text = label_text
        self.icon_path = icon_path
        self.command = command

        self.connect("clicked", self.on_button_clicked)
        self.set_size_request(400, 290)

        # Box to hold image and label
        self.load_box()

        self.set_relief(Gtk.ReliefStyle.NONE)  # Removes default button relief/padding
        self.set_border_width(0) 

        # Image
        self.load_image()

        # Label
        self.load_label()

        # Add CSS class to the button
        self.get_style_context().add_class("power-button")


    def load_box(self):
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        self.box.set_halign(Gtk.Align.CENTER)
        self.box.set_valign(Gtk.Align.CENTER)
        self.box.get_style_context().add_class("power-button-box")
        self.add(self.box)

    def load_image(self):
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(self.icon_path, width=100, height=100, preserve_aspect_ratio=True)
        self.image = Gtk.Image.new_from_pixbuf(pixbuf)
        self.image.get_style_context().add_class("power-button-icon")
        self.box.pack_start(self.image, False, False, 0)

    def load_label(self):
        self.label = Gtk.Label(label=self.label_text)
        self.label.get_style_context().add_class("power-button-label")
        self.box.pack_start(self.label, False, False, 0)
    
    def on_button_clicked(self, button):

        print(f"Executing command: {self.command}")
        # keeping this commented out while testing
        # subprocess.run(self.command, shell=True)
