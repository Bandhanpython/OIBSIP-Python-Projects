import speech_recognition as sr
import webbrowser
from datetime import datetime
import edge_tts
import asyncio
from playsound import playsound
import os

# Text To Speech 


async def speak_async(text):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")  
    await communicate.save("voice.mp3")

    playsound("voice.mp3")

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")


def speak(text):
    print("Assistant:", text)
    asyncio.run(speak_async(text))

# Voice Input


recognizer = sr.Recognizer()

def take_command():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except:

        speak("Sorry, I did not understand.")

        return ""

# Main


def main():

    speak("Hello. I am your Python Voice Assistant.")

    while True:

        command = take_command()

        if command == "":
            continue

        elif "hello" in command:

            speak("Hello Bandhan")

        elif "open google" in command:

            speak("Opening Google")

            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:

            speak("Opening YouTube")

            webbrowser.open("https://www.youtube.com")

        elif "open pinterest" in command:

            speak("Opening Pinterest")

            webbrowser.open("https://www.pinterest.com")

        elif "open chat GPT" in command or "open chat gpt" in command:

            speak("Opening ChatGPT")

            webbrowser.open("https://chat.openai.com")

        elif "time" in command:

            current_time = datetime.now().strftime("%I:%M %p")

            speak("Current time is " + current_time)

        elif "date" in command:

            today = datetime.now().strftime("%d %B %Y")

            speak("Today's date is " + today)

        elif "stop" in command or " Ok bye" in command or "exit" in command:

            speak("Goodbye, Have a nice day Bandhan.")

            break

        else:

            speak("Sorry, I don't know this command.")


if __name__ == "__main__":
    main()