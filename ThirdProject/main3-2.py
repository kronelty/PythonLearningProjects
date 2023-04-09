from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요, 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hello.mp3")

#playsound("hello.mp3")

import pygame
pygame.mixer.init()
pygame.mixer.music.load("hello.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue