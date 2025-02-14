# 📌 Voice enabled Chatbot

A Python-based chatbot that uses NLP to understand and respond to user queries. It first convert the query of the user given via voice command into a text(ASR).
This text is later then passed to an LLM to generate accurate response. This response will then converted back to audio clip and gets played to the user(TTS).

The file can be runned using the command `streamlit run app.py`
The requirements needed to build this project is specified in the `requirements.txt` file
Install those requirements using `pip install -r requirements.txt`

[Python speech recognition library](https://pypi.org/project/SpeechRecognition/),a Library for performing speech recognition, was used to convert the audio captured into text initially. Later it was replaced with Openai whisper-large-v3 which was better in performance than the later. The Large Language Model(LLM) used here is llama3-8b-8192 which is loaded and runned using groq api. [Groq](https://groq.com/) offers LLM inference via APIs which allows us to run the models with high efficiency. 

[Google Text-to-Speech](https://pypi.org/project/gTTS/) a Python library and CLI tool to interface with Google Translate text-to-speech API , was initially used to  deliver a voice version of the response. And later it was replaced by [pyttsx3 2.98](https://pypi.org/project/pyttsx3/), a Text to Speech (TTS) library for Python 3. It was far more better in performance than the later and offered many customisation on the voice generated. The user experience is maintained with the help of [Streamlit](https://streamlit.io/) which helps to build the interfaces quickly. The entire application is built upon [LangChain](https://www.langchain.com/) which is an open source framework for building applications based on large language models (LLMs).
Some of the refernce material that I have used to complete the task is attached [here](https://python.langchain.com/docs/introduction/)

# 📌 Surface Reconstruction from Point Cloud

We were given a deformed point cloud and asked to remove the deformation and reconstruct the original shape from the point cloud.

The file is named as `open3d.ipynb`. 
The requirements needed to run this file is given in `requirements.txt `, which can be installed using `pip install -r requirements.txt`.

Observations:
1. The original shape of the object was cylinder
2. There were about 3 deformations on the sufrace of the cylinder which can be considered to be misaligned points.
3. The actual shape was reconstruced and saved as `original_shape.ply` 

In this task I have used [Open3d](https://www.open3d.org/) library for visualizing the 3d data points.
Here I have initially applied some processing on the point cloud data to remove the outliers from the data. [Here](https://www.open3d.org/docs/latest/tutorial/Advanced/pointcloud_outlier_removal.html) is the tutorial that I have refered for the same. Later I have transformed the point cloud into a mesh and then tried to remove the deformations from the mesh. [This](https://www.open3d.org/docs/latest/tutorial/Advanced/surface_reconstruction.html) tutorial lead me to this. And then I applied smoothing and convex hull to remove the hole from the surface of the cylinder and obtained the original image.
[This](https://inria.hal.science/hal-01017700/document) is one of the reference materials really helped me to get a better understanding of this new concept. 
