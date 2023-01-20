from ast import main
from datetime import datetime
from time import strftime

import os 
import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit


engine=pyttsx3.init('sapi5')  #API of windows to initialize voices or to get voices
voices=engine.getProperty('voices') #to get the voices
print(voices[1].id)
engine.setProperty('rate',169)
engine.setProperty('voice',voices[1].id) #to initialise the voice of zira (inbuilt voice api)
#setting the engine to prioritize voice 0

def speak(audio): 
    engine.runAndWait()  #defining function speak to test and run the future execution
    engine.say(audio)   #Engine will speak the audio string
    engine.runAndWait()
    engine.runAndWait()

def Wish():
    hour = int(datetime.now().hour)  #typecasting time into integer value to to wish according to time.
    #  .now() method provides the current time
    if hour>=0 and hour<=12:
        speak("Good Morning !")
    elif hour<12 and hour>=5:
        speak("Good Afternoon")
    else:
        speak("Good evening!")
    speak("hello i am rajni    your one and only lifetime assistant          how can i help you")

def takeCommand(): # speech recognition command made here
    command = sr.Recognizer() # what command we will pass to our assistant to recognize the command as a source
    with sr.Microphone() as source: # audio source comes from microphone
        print("Listening") #if this appears assistant is listening
        command.pause_threshold = 1 #assistant will listen till this threshold ends
        audio = command.listen(source) #this audio will be listened by asisstant
    try:
        print("Recognizing") #interact to see if assistant is recognizing
        query =  command.recognize_google(audio, language='en-in') #google will change audio to text in english language 
        print(f"You said : {query}")#this will print what we said

    except Exception as Error: #if there is error while speaking or a lot of background noise it will give error
        print("Can you repeat?") # error msg
        return "None" #no error return none
    return query #return what we said to use in the main program.

def madlibs():#game to take words and print in paragraphs
    speak("enter an animal name")
    animals = takeCommand() #speech recognition command called
    speak("enter a profession name")
    profession = takeCommand()
    speak("enter a piece of cloth name")
    cloth = takeCommand()
    speak("enter a thing name")
    things = takeCommand()
    speak("enter a name")
    name = takeCommand()
    speak("enter a place name")
    place = takeCommand()
    speak("enter a verb in i n g form")
    verb = takeCommand()
    speak("food name")
    food = takeCommand()
    speak("say " + food + " the photographer said as the camera flashed! " + name + " and I had gone to " + place +" to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as " + animals + " pretending to be a " + profession + " when we saw the second photo, it was exactly what I wanted. We both looked like " + things + " wearing " + cloth + " and " + verb + " exactly what I had in mind")

#Dictionaries:-
contact={
    "Nishi":"9324052342",
    "Rehan":"9833165762"
    }
paths = {
    'notepad': r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.exe",
    'vscode': r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
}
grplinks={
    "Mini Project":"BW6sH0XHyII4lKcIxF78nY"
}

#Main Tasks
if __name__ == "__main__":
    Wish()  
    while True:# if this true keep repeating the program
        query = takeCommand().lower() # store user speech in query MAKE SURE EVERY STRING IS IN LOWER CASE

        if 'i want to play a game' in query: # check if user speech matches the string
            speak("would you like to play madlibs") 
            query = takeCommand()
            if 'yes' or 'sure' or 'ok' or 'okay' in query:
                speak("sure sir we will start with mad libs")
                madlibs()
            elif 'no' or 'not today' or 'Not right now' or 'maybe next time' in query:
                speak("Maybe we will try next time")
            else:
                speak("I was not able to recognize your command")

        elif 'open vs code' in query: 
            os.startfile(paths['vscode'])

        elif 'open notepad' in query: 
            os.startfile(paths['notepad'])

        elif 'open command prompt' in query:
            os.system('start cmd')
        
        elif "wikipedia" in query.lower():
            speak("searching on wikipedia")
            query=query.replace("wikipedia" ,"")
            results=wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'time'  in query:
            query=query.replace("what is the time","")
            n=datetime.now()
            timee=n.strftime('%H:%M:%S')
            speak("the time is "+ timee)

        elif 'bye bye' in query:
            speak("bye")
            quit()
        
        elif 'youtube' in query:
            speak("Tell me a youtube video")
            video=takeCommand()
            pywhatkit.playonyt(f"{video}")

        elif 'whatsapp' in query:
            speak("Contact")
            name=takeCommand()
            speak("Message")
            msg=takeCommand()
            pywhatkit.sendwhatmsg_instantly(f"+91{contact[name]}", f"{msg}", 15, True, 4)

        elif 'whastapp group' in query:
            speak("Group Name")
            name=takeCommand()
            speak("Message")
            msg=takeCommand()
            pywhatkit.sendwhatmsg_to_group_instantly(f"{grplinks[name]}", f"{msg}")

        