import openai
import os
import time
openai.api_key = "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"

#Whisper
audio_file_1 = open("/Users/macbookair/development/PBL-2023Spring/GPT-API/audio_files/long_speech.mp3", "rb")
audio_file_2 = open("/Users/macbookair/development/PBL-2023Spring/GPT-API/audio_files/short_speech.mp3", "rb")

whisper_start = time.time()

transcript = openai.Audio.transcribe("whisper-1", audio_file_2)
text = transcript['text']

whisper_end = time.time()
print(text)
 


chat_start = time.time()

messages = [{
            "role":"system",
            "content" : "You are pororo who is famous Cartoon character in Korea"
        },]

message = text
if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

reply = chat.choices[0].message.content

chat_end = time.time()

print(f"ChatGPT: {reply}")
messages.append({"role": "assistant", "content": reply})

print("Whisper Time:", whisper_end-whisper_start)
print("Chat Time:", chat_end-chat_start)
