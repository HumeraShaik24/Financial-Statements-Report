import streamlit as st
import speech_recognition as sr
import pyttsx3

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except Exception:
        return "Sorry, I did not get that."

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()