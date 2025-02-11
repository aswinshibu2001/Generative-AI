# # !/usr/bin/env python3
# # import numpy as np
# import speech_recognition as sr
# from gtts import gTTS
# import os
# import datetime
# # import transformers

# # nlp = transformers.pipeline("conversational", 
# #                             model="microsoft/DialoGPT-medium")  
# class chatbot():
#     def __init__(self,name):
#         print('------starting up ', name,'-----')
#         self.name=name

#     def speech_to_text(self):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=1)            
#             print("listening...")
#             audio = recognizer.listen(mic)
#             # print(type(audio))
#             # exit()
#         try:
#             self.text = recognizer.recognize_google(audio)
#             print("me --> ", self.text)
#         except:
#             print("me -->  ERROR")
        
#     def wake_up(self, text):
#         return True if self.name in text.lower() else False
    
    
#     @staticmethod
#     def text_to_speech(text):
#         print("ai --> ", text)
#         speaker = gTTS(text=text, lang="en", slow=False)
#         speaker.save("res.mp3")
#         os.system("start res.mp3")  
#         # os.remove("res.mp3")

#     @staticmethod
#     def action_time():
#         return datetime.datetime.now().time().strftime('%H:%M')
    

# # Run the AI
# if __name__ == "__main__":
#     ai = chatbot(name="maya")
#     while True:
#             ai.speech_to_text()
            
#             ## wake up
#             if ai.wake_up(ai.text) is True:
#                 res = "Hello I am Maya the AI, what can I do for you?"
#             ## action time
#             # elif "time" in ai.text:
#             #     res = ai.action_time()
            
#             # ## respond politely
#             # elif any(i in ai.text for i in ["thank","thanks"]):
#             #     res = np.random.choice(
#             #         ["you're welcome!","anytime!",
#             #         "no problem!","cool!",
#             #         "I'm here if you need me!","peace out!"])
        
#             ai.text_to_speech(res)


# from transformers import pipeline


# # Load a chatbot model (e.g., Mistral, LLaMA)
# pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")

# # Generate a response
# response = pipe("What is machine learning?", max_length=100)
# print(response[0]['generated_text'])

# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-V3", trust_remote_code=True)
# pipe(messages)

# Use a pipeline as a high-level helper
# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="deepseek-ai/deepseek-coder-6.7b-instruct")
pipe(messages)