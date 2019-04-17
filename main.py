from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from window import Window


class MainApp(App):
    def build(self):
        return Window().key()


if __name__ == '__main__':
    MainApp().run()
