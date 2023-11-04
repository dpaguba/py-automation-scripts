import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()

def transcribe_audio(path):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened, language="en-EN")
    return text


