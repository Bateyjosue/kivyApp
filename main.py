"""Class representing Our Main Class"""

from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    """Class representing Our main Widget"""


class BaseApp(App):
    """Class representing Our Base Widget of the Apps"""

    def build(self):
        """Build Method for building the Base App Layout"""
        return MainWidget()


if __name__ == '__main__':
    BaseApp().run()
