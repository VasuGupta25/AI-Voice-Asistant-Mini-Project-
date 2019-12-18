import  pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import os        #used for 'play music query' 
import smtplib   #python package used to send emails from gmails

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int (datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am Sophie Sir. Please tell me how may i help you")

#it takes microphone input from user and returns string output
def takeCommand(): 
    
    r=sr.Recognizer() #help in recognizing audio
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold =  1
         audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
         #print(e)   #priunts the error
         speak("Say that agian please...")   
         print("Say that agian please...")
         return "None"
    return query



def sendEmail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender_email@gmail.com', 'password')
    server.sendmail('sender_email@gmail.com', 'receiver_email@gmail.com', content)
    server.sendmail('sender_email@gmail.com', 'receiver_email@gmail.com', content)
    server.close()

if __name__ == "__main__":
    wishMe()
   
    while 1:
        query = takeCommand().lower()
    
    #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            #replacing wikipedia from query by replacing from space ie. ""
            results =  wikipedia .summary(query, sentences=2)
            #take i/p from wikipedia
            speak ("According to wikidpedia..") 
            print(results)
            speak(results) #speaks 2 sentences from wikipedia

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir= 'C:\\Users\\vasu\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))       

        elif 'time' in query:
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {currentTime}")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
      
                sendEmail(content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not that smart to do this. Make me smart!") 
        
        elif 'thank you' in query:
            speak('Your Welcome Sir')
        
        elif 'config' in query:
            speak('Hello Sir i am Sophie  I have Intel(R) Core i5-8250U Cpu @ a1.60 Gegahertz 1.80 Gegahertz ,8 GN RAM adn 63-bit Operating System and here to follow your orders until my battery dies off')
        
