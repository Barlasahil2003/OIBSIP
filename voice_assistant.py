import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Network error. Please check your connection.")
            speak("Network error. Please check your connection.")
            return ""

def get_time():
    """Return the current time."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date():
    """Return the current date."""
    today = datetime.datetime.now()
    return today.strftime("%B %d, %Y")

def search_wikipedia(query):
    """Search Wikipedia for a query and return a summary."""
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for {query}. Please be more specific."
    except wikipedia.exceptions.PageError:
        return f"No results found for {query}."

def open_website(url):
    """Open a website in the default web browser."""
    webbrowser.open(url)

# Main program
if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you?")
        elif "time" in command:
            current_time = get_time()
            print(f"The time is {current_time}.")
            speak(f"The time is {current_time}.")
        elif "date" in command:
            current_date = get_date()
            print(f"Today's date is {current_date}.")
            speak(f"Today's date is {current_date}.")
        elif "search" in command:
            query = command.replace("search", "").strip()
            print(f"Searching Wikipedia for {query}...")
            speak(f"Searching Wikipedia for {query}.")
            result = search_wikipedia(query)
            print(result)
            speak(result)
        elif "open" in command:
            url = command.replace("open", "").strip()
            print(f"Opening {url}...")
            speak(f"Opening {url}.")
            open_website(f"http://{url}")
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            print("Goodbye!")
            break
        else:
            speak("Sorry, I can't do that yet.")
