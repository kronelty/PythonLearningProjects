from gtts import gTTS

text = "안녕하세요, 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"hi.mp3")

tts2 = gTTS(text="왜 몰라도 돼", lang='ko')
tts2.save(r"babohehe.mp3")