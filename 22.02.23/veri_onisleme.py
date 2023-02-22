import csv
import speech_recognition as sr
import time
from gtts import gTTS
import os
from playsound import playsound
import pandas as pd
import pickle
# değiştirilmiş kod
import veri_onisleme
import re


class VeriOnIsleme:
    def __init__(self):
        pass

    def on_isleme(self, cumle):
        cumle = cumle.lower()
        cumle = re.sub(r'[^\w\s]', '', cumle)
        return cumle

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# create an instance of the VeriOnIsleme class
veri_onisleme = VeriOnIsleme()

# define the clean_text function as a wrapper for the on_isleme method of the VeriOnIsleme class
def on_isleme(text):
    return veri_onisleme.on_isleme(text)


import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def on_isleme(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'[^\D]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def on_isleme(text):
    # text'i küçük harflere dönüştür
    text = text.lower()

    # noktalama işaretlerini kaldır
    text = re.sub(r'[^\w\s]', '', text)

    # sayıları kaldır
    text = re.sub(r'\d+', '', text)

    # stopwords'leri kaldır
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

    # lemmatization yap
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

    return text

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


def load_model(file_path):
    """
    Scikit-learn modelini dosyadan yükler.

    Parametreler:
    file_path (str): Modelin dosya yolu.

    Döndürdüğü Değerler:
    model: Yüklenen model.
    """
    model = joblib.load(file_path)
    return model


# Kullanıcı bilgileri
email_kullanicisi = 'kullanici@gmail.com'
email_sifresi = 'sifre123'

# Veri setini yükle
veri_seti = pd.read_csv('sesli_asistan_veri_seti.csv')

# Makine öğrenimi modelini yükle
with open('model.pkl', 'rb') as dosya:
    model = pickle.load(dosya)

# Sesli asistan motorunu ayarla
ses_motoru = pyttsx3.init('sapi5')
voices = ses_motoru.getProperty('voices')
ses_motoru.setProperty('voice', voices[0].id)

# Sesli komutları anlama fonksiyonu
def komut_anla():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Nasıl yardımcı olabilirim?')
        ses_motoru.say('Nasıl yardımcı olabilirim?')
        ses_motoru.runAndWait()
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print('Komut anlaşılıyor...')
        sorgu = r.recognize_google(audio, language='tr-TR')
        print(f'Siz: {sorgu}\n')
    except Exception as e:
        print(e)
        print('Anlaşılamadı. Lütfen tekrar söyleyin...')
        return 'None'
    return sorgu

# Mesaj gönderme fonksiyonu
def mesaj_gonder(alici, konu, icerik):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_kullanicisi, email_sifresi)
        mesaj = f'Subject: {konu}\n\n{icerik}'
        server.sendmail(email_kullanicisi, alici, mesaj)
        server.quit()
        print('E-posta gönderildi.')
    except:
        print('E-posta gönderilemedi. Lütfen tekrar deneyin.')

# Hava durumu bilgisini alma fonksiyonu
def hava_durumu():
    API_key = 'API_KEY' # OpenWeatherMap API anahtarınızı girin
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    sehir = "Ankara"
    complete_url = base_url + "appid=" + API_key + "&q=" + sehir
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        sicaklik = y["temp"]
        basinc = y["pressure"]
        nem = y["humidity"]
        z = x["weather"]
        hava_durumu = z[0]["description"]
        print(f'Hava durumu: {hava_durumu}\nSıcaklık: {sicaklik} Kelvin\nBasınç: {basinc} hPa\nNem: {nem}%')
def recording():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="tr-TR")
        print(f"Anladım: {text}")
        return text
    except:
        print("Sizi anlayamadım.")
        return ""
        
        