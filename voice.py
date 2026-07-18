import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

VOICE = "en-IN-NeerjaNeural"      # English Female Voice

async def speak_async(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")

def speak(text):
    print("Friday:", text)
    asyncio.run(speak_async(text))
    