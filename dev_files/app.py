# app.py
from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
import speech_recognition as sr

# Set the path to your JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\philip.carmine\GenAIHackathon\keys\sincere-idea-402607-a9724c9ac3cd.json"

app = Flask(__name__)

# Variable to keep track of the recording state
recording = False

# Global variable to store the transcript
transcript = ""

@app.route('/')
def index():
    return render_template('index.html', transcript=transcript)

@app.route('/record', methods=['POST'])
def record_audio():
    global recording
    global transcript

    if request.form.get('action') == 'start':
        if not recording:
            recording = True
            transcript = ""  # Reset the transcript
            subprocess.run(["python", "backend.py"])
    elif request.form.get('action') == 'stop':
        recording = False
        transcript = get_transcript()

    return redirect(url_for('index'))

def get_transcript():
    recognizer = sr.Recognizer()
    audio_file = "output.wav"  # Assuming this is the filename used in backend.py

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        transcript = recognizer.recognize_google(audio_data)
        return transcript
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == '__main__':
    app.run(debug=True)
