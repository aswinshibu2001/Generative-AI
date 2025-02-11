import os
import playsound
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.runnables import RunnableLambda

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama3-8b-8192")

prompt_template = ChatPromptTemplate([
    ("system", "You are a friendly and engaging AI assistant that converses naturally with humans. Your goal is to provide helpful, thoughtful, and well-structured responses while maintaining a conversational and personable tone.Answer only to the point"),
    
    MessagesPlaceholder(variable_name="messages"),
])

# record audio from mic
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
    print(text)
    return text


# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
def call_model(state: MessagesState):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)


runnable_1 = RunnableLambda(record_audio)
runnable_2 = RunnableLambda(google_asr) 
sequence = runnable_1 | runnable_2


config = {"configurable": {"thread_id": "abc123"}}

query=sequence.invoke({})

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)

ai_message=output["messages"][-1] # output contains all messages in state
content = ai_message.content
print(content)


language='en'
myobj = gTTS(content, lang=language, slow=False)
file="audio.mp3"
myobj.save(file)
playsound.playsound(file, True)
os.remove(file)
