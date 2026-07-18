import speech_recognition as sr
import webbrowser
import subprocess
from datetime import datetime
from voice import speak

# ---------------- Speech Recognition ----------------

r = sr.Recognizer()

def takeCommand():

    with sr.Microphone() as source:

        print("\nListening...")

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

    try:

        print("Recognizing...")

        query = r.recognize_google(audio, language="en-IN")

        print("You:", query)

        return query.lower()

    except Exception:

        print("Sorry, I couldn't understand.")

        return ""

# ---------------- Websites ----------------

websites = {

    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "chatgpt": "https://chatgpt.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "whatsapp": "https://web.whatsapp.com",
    "spotify": "https://open.spotify.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "netflix": "https://www.netflix.com",
    "reddit": "https://www.reddit.com",
    "wikipedia": "https://www.wikipedia.org",
    "leetcode": "https://leetcode.com",
    "geeksforgeeks": "https://www.geeksforgeeks.org",
    "hackerrank": "https://www.hackerrank.com",
    "codechef": "https://www.codechef.com",
    "codeforces": "https://codeforces.com",
    "coursera": "https://www.coursera.org",
    "udemy": "https://www.udemy.com",
    "kaggle": "https://www.kaggle.com",
    "stackoverflow": "https://stackoverflow.com",
    "discord": "https://discord.com",
    "telegram": "https://web.telegram.org",
    "zoom": "https://zoom.us",
    "canva": "https://www.canva.com",
    "figma": "https://www.figma.com",
    "internshala": "https://internshala.com",
    "naukri": "https://www.naukri.com"
}

# ---------------- Main ----------------

if __name__ == "__main__":

    speak("Hello Anshi. I am Friday. How can I help you?")

    while True:

        query = takeCommand()

        if query == "":
            continue

        # Greetings

        if "hello" in query or "hi" in query:
            speak("Hello Anshi.")

        elif "how are you" in query or "how r u" in query:
            speak("I am doing great. Thank you for asking.")

        elif "your name" in query:
            speak("My name is Friday.")

        elif "who made you" in query:
            speak("You created me while learning Python.")

        elif "thank you" in query:
            speak("You are welcome.")

        # Time

        elif "time" in query:

            current = datetime.now().strftime("%I:%M %p")

            speak(f"The time is {current}")

        # Date

        elif "date" in query:

            today = datetime.now().strftime("%d %B %Y")

            speak(f"Today is {today}")

        # Search Google

        elif "search google" in query:

            speak("What should I search?")

            search = takeCommand()

            if search:
                webbrowser.open(f"https://www.google.com/search?q={search}")

        # Search YouTube

        elif "search youtube" in query:

            speak("What should I search?")

            search = takeCommand()

            if search:
                webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

        # Websites

        else:

            found = False

            for site in websites:

                if site in query:

                    speak(f"Opening {site}")

                    webbrowser.open(websites[site])

                    found = True

                    break

            if found:
                continue

            # Apps

            if "notepad" in query:
                speak("Opening Notepad")
                subprocess.Popen("notepad.exe")

            elif "calculator" in query:
                speak("Opening Calculator")
                subprocess.Popen("calc.exe")

            elif "paint" in query:
                speak("Opening Paint")
                subprocess.Popen("mspaint.exe")

            elif "command prompt" in query:
                speak("Opening Command Prompt")
                subprocess.Popen("cmd.exe")

            elif "file explorer" in query:
                speak("Opening File Explorer")
                subprocess.Popen("explorer.exe")

            elif "bye" in query or "exit" in query:
                speak("Goodbye Anshi. Have a wonderful day.")
                break

            else:
                speak("Sorry, I don't know that command yet.")