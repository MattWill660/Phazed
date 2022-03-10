import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.lang.builder import Builder
from phazedapp.gui.mainGUI import MainUI


class PhazedApp(App):
    """Main Application class"""

    def build(self):
        Builder.load_file("phazedapp/gui/main.kv")
        return MainUI()
