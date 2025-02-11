import streamlit as st 
import random
import time
from dotenv import load_dotenv
import os
import langchain
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama3-8b-8192")
memory=ConversationBufferMemory()

def get_memory(session_id: str):
    return ConversationBufferMemory(return_messages=True)

# Use RunnableWithMessageHistory to track chat history
chatbot = RunnableWithMessageHistory(
    model,
    get_memory,
    input_messages_key="messages",  # The key that holds the input messages
)

# Define session ID (to track user history)
session_id = "user_123"

# Simulate a chat session
messages_1 = [HumanMessage(content="Hi! I'm Bob.")]
messages_2 = [HumanMessage(content="What's my name?")]

# Get responses while maintaining memory
response_1 = chatbot.invoke({"messages": messages_1}, config={"configurable": {"session_id": session_id}})
response_2 = chatbot.invoke({"messages": messages_2}, config={"configurable": {"session_id": session_id}})

# Print chat responses in a clean format
print("\n🤖 Chatbot Responses:")
print(f"User: Hi! I'm Bob.\nBot: {response_1.content}\n")
print(f"User: What's my name?\nBot: {response_2.content}\n")

# Display stored chat history
memory = get_memory(session_id)
chat_history = memory.load_memory_variables({})  # Correct way to get stored messages

print("\n📝 Stored Chat History:\n", chat_history)






















# st.title("Simple chat")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

# # Streamed response emulator
# def response_generator():
#     response = random.choice(
#         [
#             "Hello there! How can I assist you today?",
#             "Hi, human! Is there anything I can help you with?",
#             "Do you need help?",
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)
# # Display assistant response in chat message container
# with st.chat_message("assistant"):
#     response = st.write_stream(response_generator())
# # Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})