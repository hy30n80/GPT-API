import openai
import time
import json


with open('./config.json', 'r') as f:
    config = json.load(f)

openai.api_key = config['DEFAULT']['API_KEY']

long_speech = open("/Users/macbookair/development/PBL-2023Spring/GPT-API/audio_files/long_speech.mp3", "rb")
short_speech = open("/Users/macbookair/development/PBL-2023Spring/GPT-API/audio_files/short_speech.mp3", "rb")

whisper_start = time.time()

transcript = openai.Audio.transcribe("whisper-1", short_speech)
text = transcript['text']

whisper_end = time.time()

print(text)
print("Whisper Time:", whisper_end-whisper_start)