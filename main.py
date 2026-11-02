from kivy.app import App
from kivy.uix.label import Label


class BestApp(App):
    def build(self):
        return Label(text="Hello from Best App!")


if __name__ == "__main__":
    BestApp().run()
