# 📌 Voice enabled Chatbot

"A Python-based chatbot that uses NLP to understand and respond to user queries. It first convert the query of the user given via voice command into a text(ASR).
This text is later then passed to an LLM to generate accurate response. This response will then converted back to audio clip and gets played to the user(TTS).
The file can be runned using the command ```streamlit run chatbot.py

[Python speech recognition library](https://pypi.org/project/SpeechRecognition/) is used to convert the audio captured into text which then will be fed into the LLM as a query. The Large Language Model(LLM) used here is llama3-8b-8192 which is loaded and runned using groq api. [Groq](https://groq.com/) offers LLM inference via APIs which allows us to run the models with high efficiency. 
The response from the model is passed through [Google Text-to-Speech](https://pypi.org/project/gTTS/) which will deliver a voice version of the response.
Some of the refernce material that I have used to complete the task is attached here
https://python.langchain.com/docs/introduction/"

# 📌 Surface Reconstruction from Point Cloud

"We were given a deformed point cloud and asked to remove the deformation and reconstruct the original shape from the point cloud.
Some of the reference materials really helped me to get a better understanding of this new concept, 
https://inria.hal.science/hal-01017700/document
https://www.open3d.org/html/tutorial/Advanced/surface_reconstruction.html"

