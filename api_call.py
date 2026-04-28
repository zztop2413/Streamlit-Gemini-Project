#-------THIS IS THE API FILE OF THE MAIN PROJECT THAT WILL USE API KEYS-------#
from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
from gtts import gTTS
import io #Package to handle in-memory file operations(buffer in this case for audio file not to be saved on disk)

# Load .env file
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

# Configure the Gemini API
client=genai.Client(api_key=api_key)

# Define the model explicitly
MODEL_NAME = "gemini-3-flash-preview"  # You can change this to the specific Gemini model you want to use

# Function to generate note summary and quiz questions using Gemini API for app.py(MAIN FILE):

#Note Summary and Quiz Question Generator Function:
def note_generator(images):
    
    #Prompt for generating note summary and quiz questions:
    prompt="""Summarize the picture in note format at max 100 words
    make sure to add necessary markdown to differentiate sections of the note summary."""
    
    #To Remove Delta Generator Error, we need to convert the list of images to a single image or a format that the model can process. For simplicity, let's assume we are only processing the first image in the list for now
    
    #Generate  content using client and feed it back as response to the main file:
    response=client.models.generate_content(
    contents=[images, prompt], #Feeding the image and prompt to the model to generate content
    model=MODEL_NAME 
    )
    return response.text



def audio_transcriber(text):
    
    speech=gTTS(text, lang="en", slow=False)
    #Store generated speech in an in-memory buffer instead of saving it as a file on disk
    audio_buffer=io.BytesIO() #Create an in-memory buffer to hold the audio data
    speech.write_to_fp(audio_buffer) #Write the generated speech to the in-memory buffer
    audio_buffer.seek(0) #Reset the buffer's position to the beginning after writing
    
    return audio_buffer

def quiz_generator(images, difficulty):
    prompt=""" Generate 3 quiz questions based on the content of the image with the specified difficulty level.
            Make sure to add necessary markdown to differentiate sections of the quiz questions."""
            
    response=client.models.generate_content(
        model=MODEL_NAME,
        contents=[images,prompt,difficulty]
    )
    return response.text