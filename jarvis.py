import pyttsx3
import speech_recognition as s

assist = pyttsx3.init('sapi5')
voices = assist.getProperty("voices")
print(voices)
assist.setProperty("voices", voices[0].id)

def speak(Audio):
    print(Audio)
    assist.say(Audio)
    assist.runAndWait()

def takecommand():
    sr = s.Recognizer()
    with s.Microphone as source:
        print("listening...")
        sr.pause_threshold= 1
        audio = sr.listen(source)
    
        try:
             print("Recognizing...")
             query = sr.recognize_google(audio, language='en-in')
             query = query.replace("jarvis"," ")
             print("query") 
        except Exception as error:
             speak("Sorry, internet error")
             return"None"

             return query


if __name__ == "__main__":
    query = takecommand().lower()

    if 'hello' in query:
        speak("Good morning sir")