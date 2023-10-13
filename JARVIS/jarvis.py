import pyttsx3                     #pip install  pyttsx3 
import speech_recognition as sr    #pip install  speechRecognition
import datetime
import wikipedia                   #pip install  wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[0].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
    
    speak("hi, i am Jarvis.   how may i help you")




def takeCommand():
    #it takes microphone inputs form user and returns string outputs
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1 
        audio = r.listen(source) 
        
    try:
        print("recognizing......")  
        query = r.recognize_google(audio,Language='en-in')
        print("user said: "+query)
        return query  
    
    
    except Exception as e:
#        print(e) 
        
        print("say that again please....")
        return "none"  


    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
#    speak("kiran is talented")


        if  'wikipedia' in query :
            speak('searching  wikipedia.......')
            query = query.replace("wikipedia","")
            results = wikipedia.summery(query,sentense=2)
            speak("According to wikipesia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query :
            webbrowser.open("https://www.youtube.com/")
            
        elif 'open google' in query :
            webbrowser.open("https://www.google.com/")
            
        elif 'open Sathyabama' in query :
            webbrowser.open("https://www.sathyabama.ac.in/")
            
        elif 'open sathyabamaLMS' in query :
            webbrowser.open("https://sathyabama.cognibot.in/login/index.php") 
            
            
            
            
        elif 'play music' in query :
            music_folder_path = 'D:\New folder\SONGS'
        #  music_dir = 'D:\\New folder\\SONGS'
            songs = os.listdir(music_folder_path)
            print(songs)
            os.startfile(os.path.join(music_folder_path,songs[0]))
            
            
        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,The time is {strTime}")
            
            
        elif 'open VScode' in query :
            codepath = "C:\\Users\\kiran\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath) 
            
        elif 'open cmd' in query :
            codepath1 = "%windir%\system32\cmd.exe"
            os.startfile(codepath1) 
            
            
        elif 'open Note' in query :
            notePath="C:\\Users\\KIRAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Notepad.lnk"
            os.startfile(notePath)
            try: 
                speak("speak what you want to write..")
                content = takeCommand()
            except Exception as e:
                print(e)
                
                speak("Sorry Sir , I Am not able to Write....")    
                
        elif 'Quit' in query :
            exit()
            
            
            