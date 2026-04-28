#-------THIS IS THE MAIN FILE OF THE PROJECT THAT CONTAINS ALL CODES OF STREAMLIT-------#
from api_call import note_generator, audio_transcriber, quiz_generator
from PIL import Image
import streamlit as st

#Set Title, and Description of the App:
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note Summary and Quiz Questions")
st.divider()

#Introduce Sidebar:
with st.sidebar: #c
# ──────────────────────────────────────────────────────────────
# 1. IMAGE UPLOADER AND DISPLAY
# ──────────────────────────────────────────────────────────────
    st.header("Controls")
    
    #Image Uploader:
    images=st.file_uploader("Upload photos of your note", 
                            type=["jpg","png","jpeg"],
                            accept_multiple_files=True,
                            ) #File uploader for images
    
    
    #If an image found, convert it to PIL format and store in a list:
    pill_images=[] # Create an empty list to store PIL images
    for img in images:
        pil_image=Image.open(img) # Convert each uploaded image to PIL format
        pill_images.append(pil_image) # Append(add) each PIL image to the list
        
        
    if images:
        #Warn the user if they upload more than 3 images:
        if len(images)>3:
            st.error("Please upload a maximum of 3 images.")
            
        #Create images in column format
        cols=st.columns(len(images))
        
        #Show uploaded images in the sidebar:
        st.subheader("Uploaded Images")
        
        for i, imge in enumerate(images): # index i and image imge incremented by 1 together
            with cols[i]:
                st.image(imge) #Show images in column format with captions
        
    
    #Quiz Difficulty Level Selector:
    selected_option=st.selectbox("Select Quiz Difficulty Level",
                                options=["Easy","Medium","Hard"], index=None
                                )   
    #Show the selected quiz difficulty level if user selects one:
    if selected_option:
        st.markdown(f"You have selected **{selected_option}** difficulty level for quiz questions.")
    else:
        st.error("You must choose difficulty level.")
    pressed=st.button("Click to Generate Note Summary and Quiz Questions",type="primary")
    
    
# ──────────────────────────────────────────────────────────────
# 2. MAIN PAGE : FRONT END
# ──────────────────────────────────────────────────────────────

# Error handling for image upload and quiz difficulty level selection:
if pressed:
    #If no images are uploaded, show error message:
    if not images:
        st.error("Please upload at least one image to generate note summary and quiz questions.")
    elif not selected_option:
        st.error("Please select a quiz difficulty level to generate quiz questions.")
    else:
        st.success("Images uploaded and quiz difficulty level selected successfully!")
        #Here you can add the code to generate note summary and quiz questions using the uploaded images and selected difficulty level.

        #---UPLOADED NOtE---# The code for generating note summary and quiz questions using the uploaded images and selected difficulty level will be added here in the future.---#
        with st.container(border=True):           
            st.subheader("Your Note")
        with st.spinner("Generating note summary based on the uploaded images..."):
            generated_notes = note_generator(pill_images)  # ✅ Get text first
            st.markdown(generated_notes)  
        st.divider()    
        
        
        #-----------------------------------------------------------------------------------------------------------# 
        #---AUDIO TRANSCRIPTION---#
        with st.container(border=True):
            #---UPLOADED NOtE---# The code for generating note summary and quiz questions using the uploaded images and selected difficulty level will be added here in the future.---#
            st.subheader("Your Audio Transcription")
            
            with st.spinner("Generating note summary audio based on notes..."):
                #Replace garbage audio with the generated note summary audio:
                generated_notes=generated_notes.replace("#","")
                generated_notes=generated_notes.replace("*","")
                generated_notes=generated_notes.replace("-","")
                generated_notes=generated_notes.replace("`","")
                
                audio_buffer = audio_transcriber(generated_notes)
                st.audio(audio_buffer)
                st.divider()  
            
        
        #-----------------------------------------------------------------------------------------------------------# 
        
        
        #---QUIZ---#
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty ")  # Fixed typo
            with st.spinner("Generating the quizzes "):  # ✅ FIXED: Added parentheses and message
                quizzes = quiz_generator(pill_images, selected_option)
                st.markdown(quizzes)  # Display the quizzes
            
            #TO EDIT: REPLACE THIS WITH THE CODE TO DISPLAY THE GENERATED QUIZ QUESTIONS BASED ON THE UPLOADED IMAGES AND SELECTED DIFFICULTY LEVEL.