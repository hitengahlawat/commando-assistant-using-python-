
import speech_recognition as sr 
import pyttsx3
import webbrowser
# from openai import OpenAI
import musiclibrary
import cohere
import os
import numpy as np

r = sr.Recognizer()

 
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# speak("saksham sharma ")
def aiprocesscommand(command):
    try:
        speak("it will take some time ,                                                                                                                                   be patient")
        from dotenv import load_dotenv
        load_dotenv()   
        co = cohere.ClientV2(os.getenv("CO_API_KEY" ))
        response = co.chat(
            model="command-r-plus-08-2024",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a virtual assistant named Commando, designed for general informations and tasks,you are designed and integrated by hiten gahlawat "
                        "like Alexa or Google Assistant."
                        "hiten gahlawat is an ai and ml aspirant currently persuing btech from maharaja agrasen institute of technology with degree of computer science and engineering in aiml domain"
                        "if some says play song anyone the return only the link of that song of youtuber by appling  inverted commas on both side of link "
                    )
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
                )
        return response.message.content[0].text
    
    except Exception as e:
        print(e)
        

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opeaning google for you ")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("opeaning facebook for you ")

    elif "open youtube" in c.lower():
        speak("opeaning youtuble for you ")
        webbrowser.open("https://youtube.com")
        
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("opeaning linkedin for you ")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("opeaning instagram for you ")

    elif c.lower().startswith("play"):
        speak(f"playing song for you ")
        song=aiprocesscommand(c)
        webbrowser.open(song)
        print(song)

    else:

        output=aiprocesscommand(c)
        print(output)
        speak(output)
    # else:
    #     webbrowser.open(f"https://{command}")



if __name__ == "__main__":
    speak("initializing commando")

    print("initializing commando....")
    while True:
        try:
            with sr.Microphone() as source:
                print("recognising...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source ,phrase_time_limit=3)  # Give user a bit more time
                word = r.recognize_google(audio)
            
            if  "commando" in word.lower():
                
                speak("ya")
                speak("how may i help you ")
            #listen for command
                with sr.Microphone() as source:
                    print("COMMANDO ACTIVE ...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)


        except sr.WaitTimeoutError:
            print("Timeout: No speech detected within time limit.")
            speak("Sorry, I did not hear anything.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            speak("Sorry, I could not understand your voice.")
        except sr.RequestError:
            print("Speech recognition service is unavailable.")
            speak("Sorry, service is down.")



            