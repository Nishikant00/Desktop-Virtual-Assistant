# all modules
from ast import main
from datetime import datetime
from time import strftime
import webbrowser as wb
import os 
import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia
import pywhatkit 
from time import *
import requests
from bs4 import *
from pyjokes import *
import howdoi
import smtplib
# modules end

engine=pyttsx3.init('sapi5')  #API of windows to initialize voices or to get voices
voices=engine.getProperty('voices') #to get the voices
print(voices[0].id)
engine.setProperty('rate',169)
engine.setProperty('voice',voices[0].id) #to initialise the voice of zira (inbuilt voice api)
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('addwhenneededlol@gmail.com', 'your-password')
    server.sendmail('addwhenneededlol@gmail.com', to, content)
    server.close()

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
    return query.lower() #return what we said to use in the main program.


#games
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
    
    "Nishi":"",#add phone number when wanted.
    "Rehan":""
    }
paths = {
    'notepad': r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.exe",
    'vscode': r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    'chrome':'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
}
grplinks={
    "Mini Project":"BW6sH0XHyII4lKcIxF78nY"
}

emails={
    "Nishi":""
}
# objects needed 
web=wb.get(paths['chrome'])

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

        elif 'open google' in query:          #this is to open google
            # web=wb.get(paths['chrome'])
            web.open('google.com')
        
        elif 'search on google' in query:
            speak('what should i search?')
            cmmd=takeCommand().lower()
            pywhatkit.search(cmmd)

            try:
                lines=wikipedia.summary(cmmd,sentences=2)
                speak(lines)
            except:
                speak('i guess something went wrong in searching')

            

        elif 'wait' in query:
            speak('ok')
            speak('resting for 60 seconds ')
            sleep(60)            
            speak('hey !! ')
            speak('missed me i bet you did')

        elif 'weather' in query:
            try:
                speak('Please tell me name of the city')
                city=takeCommand().lower()
                print(city)
                city='temperature in '+city
                # city='tem'
                print(city)
                url='https://www.google.com/search?q={}'.format(city)
                r=requests.get(url)
                data=BeautifulSoup(r.text,'html.parser')
                temp=data.find('div',class_='BNeawe').text
                speak('the current {} is {}'.format(city,temp))
            except Exception as e:
                print(e)
                # speak('please check your internet connection')
                speak('oops could not find it ')
                speak('please check your internet connection')

                speak('sorry for the incovinience please try again')

        elif 'joke' in query or 'bored' in query:
            joke=get_joke('en', 'all')
            speak(joke)

        elif 'email' in query:
            try:
                speak("Who do you eant to email?")
                to = f"{emails[name]}"
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Email was not sent")

        