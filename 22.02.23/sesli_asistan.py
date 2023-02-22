import os
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request
import json
from time import strftime, localtime
from gtts import gTTS
from playsound import playsound
import joblib   
import speech_recognition as sr
import random
import webbrowser
import datetime
import wolframalpha
import wikipedia
import numpy as np
import pyttsx3
import smtplib
import pandas as pd
import pickle
import pickle

# Eğitilmiş modelin yüklenmesi
with open('model.pkl', 'rb') as dosya:
    model = pickle.load(dosya)

# Daha sonra kullanılacak fonksiyonların tanımlanması ve kullanımı
...

    
    
from veri_onisleme import preprocess_text, VeriOnIsleme
from makine_ogrenimi import MakineOgrenimi
from veri_onisleme import on_isleme, clean_text
import pandas as pd

veri_seti = pd.read_csv('sesli_asistan_veri_seti.csv', header=None)
print(veri_seti)
import csv

def load_data():
    data = []
    with open('sesli_asistan_veri_seti.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Header'ı atla
        for row in reader:
            data.append(row)
    return data
def main():
    data = load_data()
    ...



# Dersi atla
def exit_function():
    assistant_response('Eğer başka bir şey yapmamı istersen buradayım.')
    exit()


# Sesli Asistanın Kullanıcının Konuşmasını Dinlemesi
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    try:
        audio_text = recognizer.recognize_google(audio, language='tr-TR')
        return audio_text.lower()
    except:
        assistant_response('Söylediğini anlayamadım, lütfen tekrar söyler misin?')
        return 0


# Kullanıcıya Yanıt Ver
def assistant_response(text):
    print(text)
    tts = gTTS(text=text, lang='tr')
    tts.save('assistant_response.mp3')
    playsound('assistant_response.mp3')
    os.remove('assistant_response.mp3')


# E-posta Gönderme
def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('seninemailadresin@gmail.com', 'sifreniz')
    server.sendmail('seninemailadresin@gmail.com', to, content)
    server.quit()


# Covid 19 Durumu
def covid_19():
    data = requests.get('https://corona.lmao.ninja/v2/all')
    data = data.json()
    infected = str(data['cases'])
    deaths = str(data['deaths'])
    recovered = str(data['recovered'])
    text = 'Dünya genelinde toplam ' + infected + ' vaka var. ' + deaths + ' insan hayatını kaybetti. ' + recovered + ' kişi iyileşti.'
    assistant_response(text)


# Wikipedia'dan Bilgi Al
def wikipedia_info(topic):
    text = 'Lütfen bekleyin, verileri topluyorum'
    assistant_response(text)
    topic = topic.replace('wikipedia', '')
    url = 'https://tr.wikipedia.org/wiki/' + topic
    webbrowser.open(url)
    text = wikipedia.summary(topic, sentences=3)
    assistant_response('Wikipedia diyor ki: ')
    assistant_response(text)


# Tarih ve Saat Bilgisi
def current_time():
    time = strftime('Saat %H:%M\nTarih %d-%m-%Y', localtime())
    assistant_response(time)


# Sesli asistan tarafından verilebilecek cevaplar
cevaplar = [
    "Tamam anladım",
    "Tabii, hemen yapacağım",
    "Elbette",
    "Anladım, hemen başlıyorum",
    "Bir dakika, hemen yapacağım",
    "Her zaman emrinizdeyim",
    "Anlayamadım, tekrar eder misiniz?",
    "Şimdilik yapamıyorum, birazdan tekrar deneyebilirim",
    "Maalesef bunu yapamam",
    "Sanırım bir hata oluştu, tekrar deneyebilir misiniz?"
]

# Ses tanıma motoru
r = sr.Recognizer()

# Asistan tarafından verilebilecek cevapları seslendirir
def cevap_seslendir(cevap):
    tts = gTTS(text=cevap, lang='tr')
    rastgele_sayi = random.randint(1, 1000000)
    dosya_ad = 'ses-' + str(rastgele_sayi) + '.mp3'
    tts.save(dosya_ad)
    playsound.playsound(dosya_ad)
    os.remove(dosya_ad)

# Sesli komutları dinler ve anlamaya çalışır
def dinle():
    with sr.Microphone() as source:
        print("Nasıl yardımcı olabilirim?")
        ses = r.listen(source)
        try:
            komut = r.recognize_google(ses, language='tr-TR')
            print(komut)
            return komut
        except sr.UnknownValueError:
            cevap_seslendir("Üzgünüm, anlayamadım.")
            return ""
        except sr.RequestError:
            cevap_seslendir("Sistem şu anda çalışmıyor.")
            return ""

# Asistanın yanıt vermesini sağlar
def cevap_ver(cevap):
    print(cevap)
    cevap_seslendir(cevap)

# İnternet bağlantısını kontrol eder
def internet_baglanti_kontrol():
    try:
        # www.google.com'a bağlanmayı dene
        webbrowser.open('https://www.google.com')
        return True
    except:
        return False

# Tarih ve saat bilgisi verir
def tarih_ve_saati_ver():
    an = datetime.datetime.now()
    tarih = an.strftime("%d %B %Y")
    saat = an.strftime("%H:%M")
    cevap = "Bugün " + tarih + " ve saat " + saat
    cevap_ver(cevap)