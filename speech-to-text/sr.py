import speech_recognition as sr

def record_volume():
    r = sr. Recognizer()
    with sr.Microphone() as source:
        print('I\'m listen to you ...')
        audio = r.listen(source)

    query = r.recognize_google(audio, language='ru-RU')
    print(f'You said: {query}.')

record_volume()