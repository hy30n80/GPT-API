import whisper
import time

long_speech = './audio_files/long_speech.mp3'
short_speech = './audio_files/short_speech.mp3'



model = whisper.load_model("base")

whisper_start = time.time()
result = model.transcribe(long_speech)

whisper_end = time.time()
print(result["text"])
print("Whisper Time:", whisper_end-whisper_start)