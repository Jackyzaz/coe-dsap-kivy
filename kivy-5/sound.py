from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader


class MusicPlayerApp(App):
    def build(self):
        # -----
        self.sound = SoundLoader.load("test.mp3")
        if self.sound:
            self.sound.play()
        # -----
        self.is_playing = False

        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        self.play_button = Button(
            text="Playing", font_size=20, size=(20, 30), size_hint=(1, 0.5)
        )
        self.play_button.bind(on_press=self.toggle_music)

        layout.add_widget(self.play_button)
        return layout

    def toggle_music(self, instance):
        if self.sound:
            if self.is_playing:
                self.sound.stop()
                self.play_button.text = "Play"
            else:
                self.sound.play()
                self.play_button.text = "Stop"
            self.is_playing = not self.is_playing


if __name__ == "__main__":
    MusicPlayerApp().run()
