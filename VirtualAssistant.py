import speech_recognition as sr
import playsound 
import random
from gtts import gTTS 
import webbrowser 
import ssl 
import certifi
import time
from time import ctime
import os #remove the audio files
import subprocess 
from PIL import Image
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
class person:
    name=""
    def setName(self,name):
        self.name=name

class assis:
    name=""
    def setName(self,name):
        self.name=name
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
def engine_speak(text):
    text=str(text)
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer()
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio=r.listen(source,5,5)
        print("Searching the Database")
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError: 
            engine_speak('Sorry mam, did not get that')
        except sr.RequestError:
            engine_speak("Sorry mam, server down")
        print(">>", voice_data.lower())
        return voice_data.lower()

def engine_speak(audio_string):
    audio_string=str(audio_string)
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,20000000)
    audio_file='audio'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(assis_obj.name +":",audio_string)
    os.remove(audio_file)

def respond(voice_data):
    #Greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet=greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)
    
    #Name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if assis_obj.name:
            engine_speak("my name is "+assis_obj.name)
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name=voice_data.split("is")[-1].strip()
        engine_speak("Okay, I will remember that "+person_name)
        person_obj.setName(person_name)

    if there_exists(["your name should be"]):
        assis_name=voice_data.split("be")[-1].strip()
        engine_speak("Okay, I will remember that my name is "+assis_name)
        assis_obj.setName(assis_name)

    #are you mad?
    if there_exists(["are you mad"]):
        assis_name=voice_data.split("mad")[-1].strip()
        engine_speak("No, but maybe you are, jo bolta hai vo hee hota hai ")
    
    #shutup
    if there_exists(["shut up"]):
        engine_speak("You shut up,.... bye ")
        exit()
    
     #shame shame?
    if there_exists(["do you have any shame"]):
        assis_name=voice_data.split("shame")[-1].strip()
        engine_speak("Yes I do. Also,.... Shame shame puppy shame, hello donkey what's your name?")

    #greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking" + person_obj.name)

    #time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[4].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)
    
    #search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term +"on google")

    if there_exists(["youtube"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term +"on youtube")
    
    if there_exists(["price of"]):
        search_term=voice_data.split("of")[-1]
        url="https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    
    # search for music
    if there_exists(["play music"]):
        search_term= voice_data.split("for")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to"+ search_term +"enjoy mam")
    #search for amazon.com
    if there_exists(["amazon .com website"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")
         
    #make a note
    if there_exists(["make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")
        
    #open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")
        
    #open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")

    # time table
    if there_exists(["show my time table"]):
        im=Image.open(r"")
        im.show()
    
    #13 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        r = random.randint(1,20000000)
        ss= "C:/Users/sharm/OneDrive/Pictures/Screenshots/" + 'ss' + str(r) + '.png'
        pyautogui.screenshot(imageFilename=ss)
        engine_speak("Screenshot saved")
        
    #weather
    if there_exists(['weather', "tell me the weather report","what's the condition outside"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    
    #open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")

      #10 stone paper scisorrs
    
    if there_exists(["rock", "paper", "scissors","game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
        cmove=random.choice(moves)
        pmove=voice_data
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    #11 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

   
    
    
    #14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        definition=definition.replace(' ','')
        sourceurl='https://dictionary.cambridge.org/dictionary/english/'+definition
        webbrowser.get().open(sourceurl)
       


    if there_exists(["exit", "quit", "bye"]):
        engine_speak("we could continue more mam, but.,,...,,,,,..,,,,, byee")
        exit()


time.sleep(1)

person_obj = person()
assis_obj = assis()
assis_obj.name = 'Assistant'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Listening") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
