import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
from os import system
import random
import time

os.system("cls")

COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}
# You can add more colors and backgrounds to the dictionary if you like.


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


# Example printing out some text
#hello = "[[red]]hello [[blue]]world[[white]]"
# print(colorText(hello))

# Example printing out an ASCII file
f = open("Ascii.txt", "r")
ascii = "".join(f.readlines())
print(colorText(ascii))


# sapi5 is speech API developed by Microsoft, helps in synthesis and
# recognition of voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")  # getting detail of current voice
# voice[0].id=Male voice and voice[1].id= female voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # without this command, speech will not be audible to us.
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    print("I am Atom, Please tell me how can I help you")
    speak("I am Atom, Please tell me how may I help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Me: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        ############################## FUN TASK ###############################

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            # return 2 sentence from wikipedia
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("youtube is opening")
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            speak("Stackoverflow is opening")
            webbrowser.open("stackoverflow.com")

        elif 'open google' in query:
            speak("Google is opening")
            webbrowser.open("google.com")

        elif "shoping" in query:
            speak("nice mood sir")
            webbrowser.open("amazon.com")
            speak("here you are sir")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'vs code' in query:
            # !Add your vs code path
            vscodePath = "C:\\Users\\CC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Vs code is opening")
            os.startfile(vscodePath)

        elif 'hello' in query:
            greetings = [
                f"hello sir, welcome"
                f"hello sir,nice to see you",
                f"welcome sir, how can i help you"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            pyttsx3.speak(greet)

        elif query.startswith('imdb'):
            show = '+'.join(query.split()[1:])
            webbrowser.open_new_tab(f"https://www.imdb.com/find?s=all&q={show}")  

        elif "open stackoverflow" in query:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif "log off" in query or "sign out" in query:
            speak(
                "Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "bye" in query:
            speak("See you later")

        else:
            speak("Can you say that again")
