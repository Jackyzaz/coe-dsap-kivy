from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.image import Image


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Image(source="pikachu.jpg", pos=(100, 100), size=(800, 500))

            # Rectangle(pos=(400, 300), size=(200, 100))


class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == "__main__":
    app = MyApp()
    app.run()
