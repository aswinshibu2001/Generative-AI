import os
import streamlit as st
from audio_handler import AudioHandler
from transcriber import Transcriber
from chat_handler import ChatHandler
import playsound

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
    # Step 1: Record audio
    file_name = audio_handler.record_audio()

    # Step 2: Transcribe audio
    query = transcriber.transcribe_audio(file_name)

    if query:
        # Step 3: Display user query
        st.chat_message("user").markdown(query)
        st.session_state.messages.append({"role": "user", "content": query})

        # Step 4: Get AI response
        response = chat_handler.get_response(query)

        # Step 5: Display AI response
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Step 6: Convert AI response to speech
        audio_file = audio_handler.text_to_speech(response)
        
        # Generate autoplay audio
        audio_html = audio_handler.autoplay_audio(audio_file)

        # Display the audio in Streamlit with autoplay
        st.markdown(audio_html, unsafe_allow_html=True)

        # Cleanup
        os.remove(audio_file)