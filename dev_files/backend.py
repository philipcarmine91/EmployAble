# backend.py
import os
import pyaudio
import wave
import speech_recognition as sr

# Set the path to your JSON key file
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\Users\philip.carmine\GenAIHackathon\keys\sincere-idea-402607-a9724c9ac3cd.json"

# Function to record audio
def record_audio(output_filename, duration=120):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
    
    frames = []

    print("Recording...")

    for _ in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()


# Function to transcribe audio
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        transcript = recognizer.recognize_google(audio_data)
        return transcript
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    output_filename = "output.wav"
    
    record_audio(output_filename)
    transcript = transcribe_audio(output_filename)

    print("Transcript:")
    print(transcript)

    # Clean up the temporary audio file
    #os.remove(output_filename)