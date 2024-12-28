import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(e)
        speak("An error occurred while trying to speak.")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print("The current time is", Time)

def date():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is", day, "/", month, "/", year)

def wishme():
    print("Welcome back Sir!")
    speak("Welcome back Sir!")
    
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")
    else:
        speak("Good Night Sir, See You Tomorrow")

    speak("Jarvis at your service Sir, please tell me how may I help you.")
    print("Jarvis at your service Sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("ss3.png")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        return query.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("Please say that again")
        return "Try Again"

    except sr.RequestError as e:
        print("Could not request results from the speech recognition service; {0}".format(e))
        speak("Sorry, I'm unable to process your request at the moment.")
        return "Try Again"

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm JARVIS created by Mr. RAGHU and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. RAGHU and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine Sir, What about you?")
            print("I'm fine Sir, What about you?")

        elif "fine" in query or "good" in query:
            speak("Glad to hear that, Sir!")
            print("Glad to hear that, Sir!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait Sir, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print(e)
                speak("Can't find this page Sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("https://www.youtube.com") 

        elif "open google" in query:
            wb.open("https://www.google.com") 
   
        elif "open stack overflow" in query:
            wb.open("https://www.stackoverflow.com")

        elif "play music" in query:
            song_dir = "C:\\Users\\NANI\\Music"
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0, x-1)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                search = takecommand()
                wb.open_new_tab(search)
                print(search)

            except Exception as e:
                print(e)
                speak("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember?")
            data = takecommand()
            speak("You told me to remember that " + data)
            print("You told me to remember that", data)
            with open("data.txt", "w") as file:
                file.write(data)

        elif "do you remember anything" in query:
            with open("data.txt", "r") as file:
                remember = file.read()
                speak("You told me to remember that " + remember)
                print("You told me to remember that", remember)

        elif "screenshot" in query:
            screenshot()
            speak("I've taken a screenshot, please check it")

        elif "offline" in query:
            speak("Goodbye Sir!")
            print("Goodbye Sir!")
            break
