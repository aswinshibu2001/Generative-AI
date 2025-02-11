# import numpy as np
import speech_recognition as sr
from gtts import gTTS
from transformers import pipeline
# import whisper
transcriber = pipeline(task="text generation")

class chatbot():
   
    def record_audio(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio=recognizer.listen(mic)     
        return audio
    

    def google_asr(self,audio):
        recognizer = sr.Recognizer()
        text=recognizer.recognize_google(audio)
        print(text)
        # return recognizer.recognize_google(audio)

    # def whispher_stt(self,audio):
    #     model = whisper.load_model("turbo")
    #     result = model.transcribe(audio)
    #     print(result["text"])

   
    

if __name__=='__main__':
    ai=chatbot()
    while True:
        audio=ai.record_audio()
        ai.google_asr(audio)