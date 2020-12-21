import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


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
        speak("Good Morning sir!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("How can I help you?")

def takeCommand():
    """It takes microphone input from user and returns string output"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
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
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open hackerrank' in query:
            webbrowser.get('chrome').open("hackerrank.com")

        elif 'play music' in query:
            music_dir = "D:\\SD Card\\songs"
            songs = os.listdir(music_dir)
            # print(songs)
            i = random.choice(list(range(830)))
            print(songs[i])
            os.startfile(os.path.join(music_dir, songs[i]))
           
            
            
        elif 'play' in query:
            music_dir = "D:\\SD Card\\songs"
            songs = os.listdir(music_dir)
            # print(songs)
            query = query.replace("play ", "")
            n = len(songs)
            for i in range(n):
                if query in songs[i]:
                    print(songs[i])
                    os.startfile(os.path.join(music_dir, songs[i]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open' in query:
            query = query.replace("open","")
            webbrowser.get('chrome').open(f"{query}.com")

        elif 'terminate' in query:
            break
            



      

    