import pyttsx3
import speech_recognition as sR
import os
import datetime
import wikipedia
import webbrowser
import random
from googlesearch import search
import os

# Usage
engine = pyttsx3.init()

def speakOut(string):
    pyttsx3.speak(string)

# Setting up Voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Adjusting Rate
rate = engine.getProperty('rate')
engine.setProperty('rate',134)

# Taking input from Microphone
def hearCommand():
    try:
        sr = sR.Recognizer()
        with sR.Microphone() as src:
            print("\nListening...")
            sr.adjust_for_ambient_noise(src, duration = 1)
            string = sr.listen(src)
    except Exception as e:
        print("Boss! I am unable to recognize your voice. Please checkout your Mic\n")        
        mic_prob = input("Press Enter to Exit\n")
    try:
        print("Recognizing...")
        inputtedString = sr.recognize_google(string, language="en-in")
        print(f"\nYou said: {inputtedString}\n")
    except Exception as e:
        return ""
    return inputtedString

def greet():
    speakOut("Hello, This is Assistant. Asmit srivastava made me for helping you in your daily life tasks")

    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        print("Don't forget to Exercise! It's better to start your day with Juices and Fresh Green Vegetables\n")
        speakOut("Good Morning Boss!")
    elif hour>=12 and hour<16:
        print("Drink plenty of Water for staying healthy\n")
        speakOut("Good Afternoon Boss!")
    elif hour>=16 and hour<20:
        speakOut("Good Evening Boss!")
    elif hour>=20 and hour<24:
        print("Please don't forget to walk at least 1500 steps after dinner\n")
        speakOut("Welcome Boss! How was your day?")
    elif hour>=0 and hour<4:
        print("I recommend you should sleep if it's not important to wake up\n")
        speakOut("Hello Boss! It's Late Night") 
    else: #adding else for just in case
        speakOut("Hello Boss!")   

    speakOut("How can I help you?")                    
                    

try:
    if __name__ == "__main__":    
        
        if '0000_user_data.txt' not in os.listdir():
            try:
                print("\nHello User! Welcome. Looks like you have sucessfully followed 'readme.txt'.\nPlease fill some details one last time\n")
                loc_music = input("Please Input your Music Directory location:\n")
                with open("0000_user_data.txt","w") as f:
                    f.write(loc_music)
                print("Great! You are good to go...\n")    
            except Exception as e:
                pass

        print("\n(C) Asmit Srivastava")
        print("Please ensure to have a proper Internet Connection\n")     

        greet()
        while True:
            inputtedString = hearCommand().lower()

            if inputtedString=="":
                pass

            elif ('play music' in inputtedString) or ('listen music' in inputtedString):
                try:
                    music_directory = loc_music # 'C:\\Users\\Asmit\\Music'
                    songs = os.listdir(music_directory)
                    print(songs)
                    randMus = random.randint(0,len(songs)-1)
                    os.startfile(os.path.join(music_directory, songs[randMus]))
                except Exception as e:
                    print("Boss I am unable to locate your music directory.\nRequest you to check on google that how to get location of any folder/partiton for your specified OS. Once you are sure that at what location i need to locate your music then kindly delete or edit '0000_user_data.txt' with your location. Apologize for the inconvenience.")    

            elif ('time' in inputtedString) or ('samay' in inputtedString):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speakOut(f"Boss the Time is {strTime}\n")
                print(strTime)

            elif ('stop' in inputtedString) or ('quit' in inputtedString):
                exit()

            elif ('shut up' in inputtedString) or ('shutup' in inputtedString) or ('mute' in inputtedString):
                pass    

            elif ('open' in inputtedString) or ('play' in inputtedString) or ('watch' in inputtedString):
                gooo_gle = search(inputtedString, num_results=10, lang="en")
                print("\n" + gooo_gle[0] + "\n")
                webbrowser.open(gooo_gle[0])

            else:
                try:
                    result = wikipedia.summary(inputtedString, sentences = 2)
                    print(result+ "\n")
                    speakOut(result)
                except Exception as e:    
                    goo_gle = search(inputtedString, num_results=10, lang="en")
                    print("\n" + goo_gle[0] + "\n")
                    webbrowser.open(goo_gle[0])

except Exception as e:
    print("Some Unexpected Error Occured. Please follow 'readme.txt' for solving it out\n")
    finish = input("Press Enter to Exit\n")