import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from googlesearch import search
import requests, json


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

# chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register("chrome" , None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning Sir!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("How can I help you?")

def takeCommand():
    """It takes microphone input from user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"You said...... {query}\n")

    except Exception as e:
        print("Say that again please.....")
        # speak("Say that again please.....")
        return "None"
    return query


if __name__ == "__main__":
    # speak("Hello sir! how's your day")
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic

        if('thank you' in query):
            speak("You are welcome sir")

        elif('introduce yourself' in query):
            speak("I am your assisstant, Jarvis. I am here to help you")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # elif 'open youtube' in query:
        #     webbrowser.get('chrome').open("youtube.com")
            
        # elif 'open google' in query:
        #     webbrowser.get('chrome').open("google.com")   

        # elif 'open hackerrank' in query:
        #     webbrowser.get('chrome').open("hackerrank.com")

        elif 'search google' in query:
            speak("What do you want me to search?")
            gs = takeCommand().lower()
            speak("Searching Google...")
            arr = list(search(gs, tld='co.in', lang='en', num=5, start=0, stop=5, pause=1.2))
            for i in arr:
                print(i)

            speak("Do you want me to open any of these??")
            
            cmd = takeCommand().lower()
            if (cmd == 'no'):
                pass
            elif('first' in cmd):
                webbrowser.get('chrome').open(arr[0])
            elif('second' in cmd):
                webbrowser.get('chrome').open(arr[1])
            elif('third' in cmd):
                webbrowser.get('chrome').open(arr[2])
            elif('fourth' in cmd):
                webbrowser.get('chrome').open(arr[3])
            elif('fifth' in cmd):
                webbrowser.get('chrome').open(arr[4])



        elif 'play a song' in query:
            music_dir = "D:\\SD Card\\songs"
            songs = os.listdir(music_dir)
            # print(songs)
            i = random.choice(list(range(845)))
            # print(songs[i])
            speak("Playing a song from your directory")
            print(songs[i])
            os.startfile(os.path.join(music_dir, songs[i]))
           
            
            
        elif 'play' in query:
            music_dir = "D:\\SD Card\\songs"
            songs = os.listdir(music_dir)
            # print(songs)
            query = query.replace("play ", "")
            n = len(songs)
            played = False
            for i in range(n):
                if query in songs[i].lower():
                    print(songs[i])
                    os.startfile(os.path.join(music_dir, songs[i]))
                    speak(f"Playing {query}")
                    played = True
            if(played == False):
                speak("I couldn't find that song.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%p:%M")    
            speak(f"Sir, the time is {strTime} minute")

        elif 'date' in query:
            fDate = datetime.datetime.now()
            day = fDate.strftime("%A")
            dat = fDate.strftime("%d:%B:%Y")
            
            speak(f"Sir, the date is {dat}! and day is {day} ")
            

        elif 'open' in query:
            query = query.replace("open","")
            speak(f"Opening {query}")
            webbrowser.get('chrome').open(f"{query}.com")

        elif 'weather' in query:
            api_key = "d65afd44e4d247347afcb07fafb75509"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Please tell your city.")
            city_name = takeCommand().lower()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
            response = requests.get(complete_url) 
            data = response.json()
            
            if data['cod'] == '404':
                speak("I can't find your city")

            else:
                y = data['main']
                temp = int(y['temp']) - 273.15
                temperature = round(temp,1)
                weath = data['weather'][0]['description']

                if 'sky' in weath:
                    weath = weath.replace(' sky', '')
                    speak(f"Sir, the current tempertaure is {temperature} degree celsius and the sky is {weath}.")
                else:
                    speak(f"Sir, the current tempertaure is {temperature} degree celsius and the weather is {weath}y.")


        elif 'terminate' in query:
            hr = int(datetime.datetime.now().hour)
            if(hr>5 and hr<21):
                speak("Have a nice day sir!")
            else:
                speak("Good Night sir")
            break