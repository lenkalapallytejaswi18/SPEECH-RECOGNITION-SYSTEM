# streamlit is used to create a web  interface 
import streamlit as st
import speech_recognition as sr

def transcribe_audio():
    recognizer = sr.Recognizer()
    #opens the microphone to record audio 
    with sr.Microphone() as source:
        #captures the user's speech 
        st.info("Listening... Speak now.")
        audio = recognizer.listen(source)
        st.success("Recording finished!")
# to recognize the audio we use recognizer 
        try:
            text = recognizer.recognize_google(audio)
            return text
#if audio was unclear or not undersatndable we use unknownvalue error 
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
# if there is any problem with internet or googe api connection
        except sr.RequestError:
            return "API unavailable or network error."

# Streamlit UI
st.title("🎙️ Speech to Text Converter") # app title 
st.write("Click the button below and start speaking...") # instructions and button 
# here the user voice will be recognized 
if st.button("Start Recording"):
    result = transcribe_audio() # call function 
    st.write("### 📝 Transcribed Text:")
    st.write(result) # to display the recognized text 
