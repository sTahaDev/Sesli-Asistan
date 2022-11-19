"""
Yapım Tarihi: 19.11.2022
Version: 1.3
"""

import time
import webbrowser
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os

#Sesi Algılama Ayarları
def record(ask = False):
    r = sr.Recognizer()
    if ask:
        speak(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Üzgünüm! Sistem Çalışmıyor :(")

        return voice

#Koşullandırma
def response(voice):
    voice = voice.lower()
    if "nasılsın" in voice:
        speak("İyiyim Teşekkürler")
    elif "saat kaç" in voice:
        saatTR = datetime.now().strftime("%H,%M,%S")
        print("Saat: "+saatTR)
        speak(saatTR)
    elif "araştır" in voice:
        print("Eklemeler sadece youtube için geçerlidir")
        search = record("Ne aramak istiyorsun ?")
        url = "https://google.com/search?q="+search
        print("Bu kadar mı?")
        speak("Bu Kadar mı?")
        ekleme = record()
        if "evet" in ekleme:
            webbrowser.get().open(url);
        else:
            speak(search+" için devam edin")
            ekleme2 = record()
            url = "https://www."+search+".com/results?search_query="+ekleme2
            webbrowser.get().open(url);

        speak(f"{search} için bulduklarım: ")
    elif "tamamdır" in voice:
        speak("Görüşmek Üzere...")
        exit()
    elif "bugün günlerden ne" in voice:
        gun = datetime.now().strftime('%A')
        print(gun)
        if gun == "Sunday":
            speak("Bu gün günlerden Pazar")
        elif gun == "Monday":
            speak("Bu gün günlerden Pazartesi")
        elif gun == "Tuesday":
            speak("Bu gün günlerden Salı")
        elif gun == "Wednesday":
            speak("Bu gün günlerden Çarşamba")
        elif gun == "Thursday":
            speak("Bu gün günlerden Perşembe")
        elif gun == "Friday":
            speak("Bu gün günlerden Cuma")
        elif gun == "Saturday":
            speak("Bu gün günlerden Cumartesi")

#Konuşturma
def speak(string):
    tts = gTTS(string,lang="tr")
    rand = random.randint(1,10000)
    file = "audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
    
time.sleep(1)
print("Nasıl Yardımcı Olabilirim ?")
speak("Buyrun Efendim")
while 1:
    print("Dinliyorum...")
    speak("Dinliyorum")
    ses = record()
    print(ses)
    response(ses)

