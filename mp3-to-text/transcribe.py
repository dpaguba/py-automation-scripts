import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav
sound = AudioSegment.from_mp3("transcript.mp3")
sound.export("transcript.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "transcript.wav"

