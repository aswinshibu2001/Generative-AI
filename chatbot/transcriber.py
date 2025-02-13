from groq import Groq
import config
import os

class Transcriber:
    def __init__(self):
        self.client = Groq(api_key=config.API_KEY)

    def transcribe_audio(self, file_name):
        # converts the audio to text using whispher model
        try:
            with open(file_name, "rb") as file:
                response = self.client.audio.translations.create(
                    file=(file_name, file.read()),
                    model="whisper-large-v3",
                    prompt="Specify context or spelling",
                    response_format="json",
                    temperature=0.0
                )
            print("Transcription:", response.text)
            os.remove(file_name)
            return response.text
        except Exception as e:
            print(f"Error in transcription: {e}")
            return None


    