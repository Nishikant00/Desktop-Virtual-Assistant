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
from random import *
import pyautogui
import openai
# *modules end*

############################ THE HEART ###########################################################################3
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

# def takeCommand(): # speech recognition command made here
#     command = sr.Recognizer() # what command we will pass to our assistant to recognize the command as a source
#     with sr.Microphone() as source: # audio source comes from microphone
#         print("Listening") #if this appears assistant is listening
#         command.pause_threshold = 1 #assistant will listen till this threshold ends
#         audio = command.listen(source) #this audio will be listened by asisstant
#     try:
#         print("Recognizing") #interact to see if assistant is recognizing
#         query =  command.recognize_google(audio, language='en-in') #google will change audio to text in english language 
#         print(f"You said : {query}")#this will print what we said

#     except Exception as Error: #if there is error while speaking or a lot of background noise it will give error
#         print("Can you repeat?") # error msg
#         return "None" #no error return none
#     return query.lower() #return what we said to use in the main program.
def takeCommand(): # speech recognition command made here
    command = sr.Recognizer() # what command we will pass to our assistant to recognize the command as a source
    with sr.Microphone() as source: # audio source comes from microphone
        print("Listening") #if this appears assistant is listening
        command.pause_threshold = 0.8 #assistant will listen till this threshold ends
        audio = command.listen(source) #this audio will be listened by asisstant
    try:
        print("Recognizing") #interact to see if assistant is recognizing
        query =  command.recognize_google(audio, language='en-in') #google will change audio to text in english language 
        print(f"You said : {query}")#this will print what we said

    except Exception as Error: #if there is error while speaking or a lot of background noise it will give error
        print("Can you repeat?") # error msg
        return "None" #no error return none
    return query.lower() #return what we said to use in the main program.

################################################HEART END #####################################################3333


def convert(a):
    if a=='one':
        return 1
    elif a=='two':
        return 2
    elif a=='three':
        return 3
    elif a=='four':
        return 4
    elif a=='five':
        return 5
    elif a=='six':
        return 6
    elif a=='seven':
        return 7
    elif a=='eight':
        return 8
    elif a=='nine':
        return 9
    elif a=='ten':
        return 10
    elif a=='twenty':
        return 20
    elif a=='fifty':
        return 50
    else:
        speak('as i could not get what you meant')
        speak('applying default as 5') 
        return 5   
    

def writejava():
        pyautogui.press('win')
        sleep(1)
        pyautogui.typewrite('notepad')
        sleep(1)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.hotkey('win','up')
        sleep(1)
        pyautogui.typewrite(
            '''
            import java.lang.*;

            class demo
            {
                public static void main(String x[])
                {
                    int a=6;
                    int b=9;

                    System.out.println("Addition="+(a+b));
                    System.out.println("thank you");
            
                }  
            }''',interval=0.1
        )

def writesort():
 
    pyautogui.press('win')
    sleep(0.8)
    pyautogui.typewrite('notepad')
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.hotkey('win','up')
    sleep(1)
    {
            

    }
    pyautogui.typewrite(
        '''#include <stdio.h>

    void mergesort(int a[],int lb,int ub)
    {
        int m;
        if(lb<ub)
        {
            m=(lb+ub)/2;
            mergesort(a,lb,m);
            mergesort(a,m+1,ub);
            merge(a,lb,m,ub);
        }
    }

void merge(int a[],int lb,int m,int ub)
{
    int i,j,temp[100],k=0;
    i=lb;
    j=m+1;
    while(i<=m && j<=ub)
    {
        if(a[i]<a[j])
        {
            temp[k]=a[i];
            i++;
            k++;
        }
        else{
            temp[k]=a[j];
            j++;
            k++;
            
        } 
    }
    while(i<=m)
    {
        temp[k]=a[i];
        i++;
        k++;
        
    }
    while(j<=ub)
    {
        temp[k]=a[j];
        j++;
        k++;
        
    }
    k=0;
    for(i=lb;i<=ub;i++)
    {
        a[i]=temp[k];
        k++;
    } 
}

int main() {
int a[100],n,i;

printf("enter number of terms=");
scanf("%d",&n);

for(i=0;i<n;i++)
{
    printf("enter number=");
    scanf("%d",&a[i]);
}

mergesort(a,0,n-1);
for(i=0;i<n;i++)
{
printf("%d\t",a[i]);
}
return 0;
}''',interval=0.01
        
        )
    
def basetemplate():
    speak('thats awesome')

    pyautogui.press('win')
    sleep(0.5)
    pyautogui.typewrite('vs code')
    sleep(2)
    pyautogui.press('enter')
    sleep(8)
    pyautogui.hotkey('ctrl','alt','win','n')
    while True:
        speak('please tell me a file name')
        filename=takeCommand()
        if filename=='None':
            speak('please tell again')
            filename=takeCommand()
        else:
            break

    sleep(4)
    pyautogui.typewrite('{}.java'.format(filename))
    sleep(0.7)
    pyautogui.press('enter')
    pyautogui.typewrite('{}.java'.format(filename))
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.hotkey('win','up')
    sleep(3)
    pyautogui.typewrite(
            '''
import java.lang.*;
            import java.util.*;

            
            class rajni
            {
                public static void main(String x[])
                {
                Scanner sc = new Scanner(System.in);
                int a=sc.nextInt();
                int b=sc.nextInt();
                System.out.println("Addition="+(a+b));
                        
                }  
            }
            ''',interval=0.05
        )
    speak('sorry but i am not able to change the class name , please change it or java will euin your day')



#####################################################games
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

###############################################Dictionaries:-####################################################
contact={
    
    "Nishi":"9324052342",
    "Rehan":"9833165762"
    }
paths = {
    'notepad': r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.exe",
    'vscode': r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    'chrome':'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
}
grplinks={
    "Mini Project":"BW6sH0XHyII4lKcIxF78nY"
}


###############################################################################################
############# THE API ARENA ##################################################################
apidicts={
    'buisness':'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ba2ab861b54941bea14c5091d917a498',

    'sports':'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ba2ab861b54941bea14c5091d917a498',

    'entertainment':'https://newsapi.org/v2/top-entertainment?country=in&category=business&apiKey=ba2ab861b54941bea14c5091d917a498',

    'science':'https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ba2ab861b54941bea14c5091d917a498',

    'technology':'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ba2ab861b54941bea14c5091d917a498',
    'general':
    'https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=ba2ab861b54941bea14c5091d917a498',



}

API_KEY_chatgpt='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'
openai.api_key = API_KEY_chatgpt

def do(txt):
    response = openai.Completion.create(model="text-davinci-003", 
                                        prompt=txt, 
                                        temperature=0,
                                          max_tokens=1024
                                        )
    r=response.choices[0].text
    return r

def get_latest_news(cat):
    news_headlines = []
    res = requests.get(
        apidicts[cat]).json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

movie_api_key="https://api.themoviedb.org/3/trending/movie/day?api_key=a1e8dcd8749c1d0d4bd827cf5e246b57"

def get_trending_movies():
    trending_movies = []
    res = requests.get(
        movie_api_key).json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]




############################################################################################################

web=wb.get(paths['chrome'])

tp=['working on it soon','fetching some good results for you','here is what i found ']

############################################Main Tasks#############################################################
if __name__ == "__main__":
    Wish()  

    speak('before starting up please make sure u have troubleshooted the microphone from settings')
    speak('please do till the time i will take rest')
    while True:# if this true keep repeating the program
        query = takeCommand().lower() # store user speech in query MAKE SURE EVERY STRING IS IN LOWER CASE
        # query=input('enter query=')
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

        # elif 'open vs code' in query: 
        #     os.startfile(paths['vscode'])


        elif 'who are you ' in query:
            speak('my name  is rajni')
            speak('i was built by some mad peoplefor their project')

        

        # elif 'open notepad' in query: 
        #     os.startfile(paths['notepad'])

        elif 'open command prompt' in query:
            os.system('start cmd')
        
        elif "wikipedia" in query or 'who' in query:
            try:
                speak("searching on wikipedia")
                query=query.replace("wikipedia" ,"")
                results=wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
            except:
                speak('ooooops   sorry i think something  went wrong')

        elif 'time'  in query:
            query=query.replace("what is the time","")
            n=datetime.now()
            timee=n.strftime('%H:%M:%S')
            speak("the time is "+ timee)

        elif 'bye bye' in query or 'bye' in query:
            speak("bye")
            quit()

        
        
        elif 'youtube' in query:
            try:
                speak("Tell me a youtube video")
                video=takeCommand()
                pywhatkit.playonyt(f"{video}")
            except:
                speak('i think the internet connection is  not proper')
                speak('please try connecting again')


        elif 'whatsapp' in query:
            try:
                speak("Contact")
                name=takeCommand()
                speak("Message")
                msg=takeCommand()
                pywhatkit.sendwhatmsg_instantly(f"+91{contact[name]}", f"{msg}", 15, True, 4)
            except:
                speak('i think the internet connection is  not proper')
                speak('please try connecting again')

        elif 'whastapp group' in query:
            try:
                speak("Group Name")
                name=takeCommand()
                speak("Message")
                msg=takeCommand()
                pywhatkit.sendwhatmsg_to_group_instantly(f"{grplinks[name]}", f"{msg}")
            except:
                speak('i think the internet connection is  not proper')
                speak('please try connecting again')

        elif 'open google' in query:          #this is to open google
            # web=wb.get(paths['chrome'])
            web.open('google.com')
        
        elif 'search on google' in query:
            try:
                speak('what should i search?')
                cmmd=takeCommand().lower()
                pywhatkit.search(cmmd)
            except:
                speak('i think the internet connection is  not proper')
                speak('please try connecting again')

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

        elif 'news' in query or 'khabar' in query:
            
            try:
                speak('which news would you like to listen?')
                speak('sports or buisness or entertainment or science or technology')
                speak('or would you like to listen all general news?')
                task=takeCommand().lower()
                # task=input("enter=")
                cat='general'
                if 'science' in task :
                    cat='science'
                elif 'sports' in task or 'cricket' in task:
                    cat='sports'
                elif 'entertainment' in task :
                    cat='entertainment'
                elif 'buisness' in task :
                    cat='buisness'
                elif 'technology' in task:
                    cat='technology'
                elif 'general' in task:
                    cat='general'


                listofnews=get_latest_news(cat)
                print(listofnews)
                speak(choice(tp))
                for i in listofnews:
                    speak(i)

            except:
                speak('i think the internet connection is  not proper')
                speak('please try connecting again')


        elif 'movies' in query:
            movies=get_trending_movies()
            speak(choice(tp))
            speak('here are some top trending movies for you')
            for i in movies:
                print(i)
                speak(i)

        #volume control
        #numbers problem: sometimes string, sometimes number string, sometimes none
        elif 'volume up' in query:
            speak("By how much?")
            num=takeCommand().lower()
            if num.isdigit():
                for r in range(int(num)//2):
                    pyautogui.press("volumeup")
            else:
                number=convert(num)
                for r in range(number//2):
                    pyautogui.press("volumeup")
        
        elif 'volume down' in query:
            speak("By how much?")
            num=takeCommand().lower()
            # num=int(input("enter number="))
            if num.isdigit():
                for r in range(int(num)//2):
                    pyautogui.press("volumedown")
            else:
                number=convert(num)
                for r in range(number//2):
                    pyautogui.press("volumedown")
        
        elif 'mute the volume' in query:
            pyautogui.press("volumemute")

        #screenshot
        elif 'screenshot' in query:
            screen_shot = pyautogui.screenshot()
            speak('what would you like to name it?')
            name=takeCommand().lower()
            screen_shot.save(f'{name}.png')

        #copy and paste lol
        elif 'select all'in query:
            pyautogui.hotkey('ctrl', 'a')

        elif 'copy' in query:
            pyautogui.hotkey('ctrl', 'c')
        
        elif 'paste' in query:
            pyautogui.hotkey('ctrl', 'v')

        elif 'notepad' in query:
            speak(choice(tp))

            pyautogui.press('win')
            sleep(1)
            pyautogui.typewrite('notepad')
            sleep(1)
            pyautogui.press('enter')
            sleep(2)
            pyautogui.hotkey('win','up')
            # pyautogui.typewrite('hellohello')

        elif 'thank you' in query:
            speak('u are always welcome')

        # elif 'notepad plus plus' in query:
        #     speak(choice(tp))

        #     pyautogui.press('win')
        #     pyautogui.typewrite('notepad++')
        #     sleep(1)
        #     pyautogui.press('enter')

        elif 'vs code' in query or 'visual studio code' in query:
            speak(choice(tp))

            pyautogui.press('win')
            pyautogui.typewrite('vscode')
            sleep(1)
            pyautogui.press('enter')
            sleep(3)
            pyautogui.hotkey('win','up')

        elif 'settings' in query:
            speak(choice(tp))

            pyautogui.press('win')
            sleep(2)
            pyautogui.typewrite('settings')
            sleep(1)
            pyautogui.press('enter')

        elif 'camera' in query:
            speak(choice(tp))

            pyautogui.press('win')
            sleep(2)
            pyautogui.typewrite('camera')
            sleep(1)
            pyautogui.press('enter')
            speak('smile please')
            sleep(4)
            
            pyautogui.press('enter')


        elif 'file explorer' in query:
            speak(choice(tp))


            pyautogui.press('win')
            sleep(2)
            pyautogui.typewrite('file explorer')
            sleep(1)
            pyautogui.press('enter')
            sleep(1)
            pyautogui.hotkey('win','up')

        elif 'calculator' in query:
            speak(choice(tp))

            pyautogui.press('win')
            sleep(2)
            pyautogui.typewrite('calculator')
            pyautogui.press('enter')

        elif 'write a java program' in query:
            speak('that seems interesting')
            speak(choice(tp))

            writejava()

        elif 'write a sorting program' in query:
            speak('writing in c language')
            sleep(0.2)
            writesort()

        elif 'create a base template' in query:
            basetemplate()

        elif 'write a program' in query:
            speak('ok')
            txt=query
            text=do(txt)
            # print(text)
            pyautogui.press('win')
            sleep(2)
            pyautogui.typewrite('notepad')
            sleep(2)
            pyautogui.press('enter')
            sleep(2)
            pyautogui.hotkey('win','up')
            sleep(2)
            pyautogui.typewrite(text,interval=0.02)
            speak('i hope its correct')




        del(query)
##############################   END ###########################################################
#########################################################################################################################        