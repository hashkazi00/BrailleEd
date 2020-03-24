import gi
import pyttsx3
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk
engine = pyttsx3.init()
engine.setProperty('rate', 150)    
engine.setProperty('volume', 1)
import threading

class BrailleEd(Gtk.Window):
    def _init_(self):
        Gtk.Window._init_(self,title="BrailleEd")
        self.set_border_width(16)
        self.set_default_size(640,480)
        self.set_resizable(False)
        self.set_icon_from_file("/Users/hashkazi/Desktop/screen.png")
        
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)
        
        hb = Gtk.HeaderBar()
        hb.props.title = "BrailleEd"
        self.set_titlebar(hb)
        
        self.b1 = Gtk.Button(label="KEY1")
        self.b1.connect('clicked', self.Start)
        self.vbox.pack_start(self.b1, True, True, 0)
        
    def Start(self,widget, duration = 10):
        engine.say("Welcome to Digi Vision")
        engine.runAndWait()
        t=threading.Thread(target=Start)
        t.start()
        
        
css = b"""
window.background {
    background: #000000;
}
headerbar, headerbar button { 
    background: #FFFFFF;
    color: black;
}
"""

style_provider = Gtk.CssProvider()
style_provider.load_from_data(css)
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_USER
)
        
        
        
        
        
win=BrailleEd()  
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()