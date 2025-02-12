import streamlit as st
import speech_recognition as sr
import random
import time

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def record_audio(_input=None):
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Recording... Speak now!")
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        audio=recognizer.listen(mic)     
    return audio
# convert the audio to text
def google_asr(audio):
    recognizer = sr.Recognizer()
    text=recognizer.recognize_google(audio)
    # print(text)
    return text

if st.button("🎤 Start Recording"):
    audio=record_audio()
    if audio:
        text=google_asr(audio)
        st.session_state.messages.append({"role": "user", "content": text})
        # st.rerun()
