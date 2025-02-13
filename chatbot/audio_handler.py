import os
import speech_recognition as sr
import pyttsx3
import base64

class AudioHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_audio(self):
        """Records audio from microphone and saves it."""
        with sr.Microphone() as mic:
            print("Recording... Speak now!")
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = self.recognizer.listen(mic)

        file_name = "result.mp3"
        with open(file_name, "wb") as f:
            f.write(audio.get_wav_data())
        return file_name

    def text_to_speech(self, text, file_name="audio.mp3"):
        """Converts text to speech and saves the file."""
        engine = pyttsx3.init()
        engine.save_to_file(text, file_name)
        engine.runAndWait()
        return file_name

    def autoplay_audio(self,file_path):
        """Generates an HTML snippet to autoplay audio."""
        with open(file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            b64_audio = base64.b64encode(audio_bytes).decode()
            html_code = f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
                </audio>
            """
            return html_code