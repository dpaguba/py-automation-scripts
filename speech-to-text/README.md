# Voice Recording and Transcription Script 📝

This Python script allows you to record audio using your computer's microphone and transcribe it into text using the SpeechRecognition library and the Google Web Speech API.

## Getting Started

1. Make sure you have the required Python libraries installed. You can install them using pip:
    ```
    pip install -r requirements.txt
    ```
2. Run the script using the following command:
    ```
    python transcribe.py
    ```
3. The script will listen to your voice, transcribe it into text, and print the transcribed text in the console.

## Script Usage

This script contains the following main function:

- `record_volume()` - Records audio from the microphone and transcribes it into text. By default, the script uses the "ru-RU" language for transcription.

## Customize the Script

- You can change the transcription language by modifying the `language` parameter in the `r.recognize_google()` function. For example, you can use "en-US" for English or another language code supported by the Google Web Speech API.

- Customize the script to save the transcribed text to a file, integrate it into a larger project, or trigger actions based on the transcribed voice command.



