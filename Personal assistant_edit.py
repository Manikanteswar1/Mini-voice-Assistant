import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Mani!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Mani!")
    else:
        speak("Good Evening Mani!")

    speak("I am your Personal assistant. How can I help you today?")

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand. Could you repeat that?")
        speak("Sorry, I did not understand. Could you repeat that?")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;")
        speak("Sorry, I could not connect to the recognition service.")
        return ""

def main():
    wish_me()

    while True:
        query = listen_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia, ")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No page found for the query.")
            except Exception as e:
                speak("An error occurred while fetching data from Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")
            speak("Opening Stack Overflow")

        elif 'play music' in query:
            music_dir = "D:\songs"
            if os.path.isdir(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music")
                else:
                    speak("No songs found in the music directory.")
            else:
                speak("Music directory not found.")

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'quit' in query or 'bye' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
