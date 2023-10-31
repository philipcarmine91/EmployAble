import pyaudio
import wave
import keyboard  # Keyboard library is used to detect keypress
import speech_recognition as sr
import time
import os
import pyttsx3
import openai
import docx
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from os.path import expanduser
import sys
import CreateCoverLetterIndex
import CreateCVIndex

if __name__ == "__main__":
    audio_file_path = "recorded_audio.wav"
    engine = pyttsx3.init()
    welcome_text = "Hello, welcome to your virtual careers advisor. My name is Stephen, and I am going to be your careers advisor for today. I can help you with a number of things. I can help you to write a CV, to write a cover letter if you have a particular job that you are interested in or you can have a chat with me if you have some general career questions or are not sure what direction to take in your career. To generate a CV, press '1'. To develop a cover letter for a job that you are interested in applying for, press '2'. If you just want to have a chat or want some advice, please press '3'"
    print(welcome_text)
    engine.say(welcome_text)
    engine.runAndWait()
    keyboard.read_key()
    if keyboard.is_pressed('3'):
        print("option currently not available")
    elif keyboard.is_pressed('2'):
        CreateCoverLetterIndex.main()
    elif keyboard.is_pressed('1'):
        CreateCVIndex.main()