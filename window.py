from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Window(GridLayout):
    def key(self):
        return Button(text='ddd')
