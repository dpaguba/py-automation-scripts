# Audio Transcription Script 🎙️📝

This Python script provides a convenient way to transcribe audio files into text using the SpeechRecognition library. It can handle large audio files by splitting them into smaller segments based on silence.

## Getting Started

1. Make sure you have the required Python libraries installed. You can install them using pip:
    ```
    pip install -r requirements.txt
    ```
2. Download and save your audio file (e.g., "test.mp3") in the same directory as the script.
3. Run the script using the following command:
    ```
    python transcribe.py
    ```
4. The script will transcribe the audio and print the results in the console. The output will be both visualized and saved as a text file.

## Script Usage

This script consists of two main functions:

1. `transcribe_audio(path)` - Transcribes a single audio file (WAV format) given its file path. It utilizes the Google Web Speech API to perform the transcription.

2. `get_large_audio_transcription_on_silence(path)` - Splits a large audio file into smaller segments based on silence and transcribes each segment. This function is suitable for handling lengthy audio files effectively.

## Customize the Script

- You can modify the script to work with other audio formats if needed by adjusting the `AudioSegment.from_file()` function to load the appropriate format.

- Fine-tune the silence detection parameters to suit your audio files by modifying the `min_silence_len` and `silence_thresh` values in the `get_large_audio_transcription_on_silence()` function.
