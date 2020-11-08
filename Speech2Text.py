import speech_recognition as sr
from time import *
from playsound import playsound
import os
from gtts import gTTS
import pyttsx3
import webbrowser


def convertClientAudio():
    r = sr.Recognizer()
    result = ""
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
        try:
            result = r.recognize_google(audio)
        except Exception as error:
            convertClientAudio()
    result = result.lower()
    return result


def response(clientString): 
    response = ""
    if "how are you" in clientString :
        response = "I am doing well! How are you?"
    elif "i'm not doing so well" in clientString:
        response = "Why do you think that is?"
    elif "i have been thinking negatively lately" in clientString:
        response = "What happened that you have been thinking negatively"
    elif "i've been under alot of stress lately" in clientString:
        response = "How do you cope with the stress that this gives you?"
    elif "i've been avoiding the things that give me stress" in clientString:
        response = "that is a good way. always take a break"
    elif "i've been talking to my friends more to deal with my stress" in clientString:
        response = "that is a good way to cope with your stress. but make sure they are nice people"
    elif "i think i have a problem" in clientString:
        response = "what do you believe the source of your problem is"
    elif "i think it is my off mood" in clientString:
        response = "then lets think of things that will bring you to a happy mood"

    return response


def speak(text):
    # sleep(10)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()