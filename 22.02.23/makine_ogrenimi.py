import speech_recognition as sr
import time
from gtts import gTTS
import os
from playsound import playsound
import pandas as pd
import pickle


def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım, tekrar söyler misin?")
        except sr.RequestError:
            speak("Üzgünüm, şu anda hizmet veremiyoruz")
        return voice_data


def speak(text):
    tts = gTTS(text=text, lang="tr")
    filename = "speak.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)


def process_text(text):
    text = text.lower()
    return text


def assistant():
    speak("Sana nasıl yardımcı olabilirim?")
    while True:
        voice_data = record_audio()
        text = process_text(voice_data)
        if "selam" in text:
            speak("Merhaba, nasıl yardımcı olabilirim?")
        elif "nasılsın" in text:
            speak("İyiyim, teşekkür ederim. Sen nasılsın?")
        elif "saat kaç" in text:
            current_time = time.strftime("%H:%M", time.localtime())
            speak(f"Şu anki saat {current_time}")
        elif "görüşürüz" in text:
            speak("Görüşmek üzere, hoşça kalın!")
            break
        else:
            speak("Üzgünüm, anlamadım. Lütfen tekrar söyler misiniz?")


if __name__ == "__main__":
    assistant()

