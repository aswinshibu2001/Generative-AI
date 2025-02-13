import os
import streamlit as st
from audio_handler import AudioHandler
from transcriber import Transcriber
from chat_handler import ChatHandler


# Initialize handlers
audio_handler = AudioHandler()
transcriber = Transcriber()
chat_handler = ChatHandler()




st.title("Simple Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.button("🎤 Start Recording"):
    # step 1: record audio
    file_name = audio_handler.record_audio()

    # step 2: convert audio to txt
    query = transcriber.transcribe_audio(file_name)

    if query:
        # step 3: display user query
        st.chat_message("user").markdown(query)
        st.session_state.messages.append({"role": "user", "content": query})

        # step 4: get the response from llm
        response = chat_handler.get_response(query)

        # step 5: display the response
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # step 6: convert the response to speech
        audio_file = audio_handler.text_to_speech(response)
        
        # generate autoplay audio
        audio_html = audio_handler.autoplay_audio(audio_file)

        # display the audio in streamlit with autoplay
        st.markdown(audio_html, unsafe_allow_html=True)

        
        os.remove(audio_file)