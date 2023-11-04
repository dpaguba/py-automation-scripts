import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()
