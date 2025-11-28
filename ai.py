import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import keyboard
import random
import sounddevice as sd
import numpy as np
import pyautogui
import time
import cv2
import subprocess
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
def listen_for_clap():
    print(Fore.YELLOW+"Please clap to start...")
    while True:
        audio_data = sd.rec(int(44100 * 0.5), samplerate=44100, channels=2, dtype=np.int16)
        sd.wait()
        if np.max(np.abs(audio_data)) > 1000:  # Adjust this threshold based on your environment
            print(Fore.RED+"Clap detected!")
            break

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning sir,what can i do for you")
    elif 12 <= hour < 18:
        speak("Good afternoon sir,what can i do for you")
    else:
        speak("Good evening sir,what can i do for you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
          print(Fore.GREEN+"Listening...")
          r.pause_threshold = 1
          audio = r.listen(source, 0, 10)
    try:
        print(Fore.YELLOW+"Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(Fore.BLUE+f"user said:{query}\n")
    except Exception as e:
        print(Fore.RED+"say that again please")
        speak("say that again please")
        return'continue'
    return query
if __name__ == '__main__':
  while True:
     listen_for_clap()
     wishme()
     while True:
      query=takecommand().lower()
      if'wikipedia'in query:
          speak('searching please wait')
          query=query.replace("wikipedia", '')
          results=wikipedia.summary(query,sentences=2)
          speak("according to internet")
          print(Fore.GREEN+results)
          speak(results)

      elif'open youtube'in query:
            webbrowser.open("https://www.youtube.com/")

      elif'open google'in query:
            webbrowser.open("https://www.google.com/")
            
      elif'open zoom' in query:
          subprocess.call('C://Users//laxmi//AppData//Roaming//Zoom//bin//Zoom.exe')
      elif'open whatsapp' in query:
          webbrowser.open("web.whatsapp.com")
      elif'open camera' in query:
           cap = cv2.VideoCapture(0)

           if not cap.isOpened():
             print("Error: Could not open camera.")
             exit()

           while True:
                 ret, frame = cap.read()
                 if not ret:
                     print("Error: Failed to capture frame.")
                     break

                 cv2.imshow("Camera", frame)

                 # Break the loop if 'q' key is pressed
                 if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
           cap.release()
           cv2.destroyAllWindows()

      elif'open email'in query:
          webbrowser.open('mail.google.com')
          speak("done sir")
      elif'open herbalife'in query:
          webbrowser.open('https://accounts.myherbalife.com/?appId=1&locale=en-IN&redirect=https://www.myherbalife.com/')
          speak("done sir")
      elif'open map'in query:
          webbrowser.open('maps.google.com')
          speak("done sir")
      elif'open spotify'in query:
          os.startfile('C:\\Users\\laxmi\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe')
          speak("done sir")
      elif 'play song' in query:
          while True:
                    music_dir = 'music'
                    songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav', '.ogg', '.flac'))]

                    if songs:
                            random_song = random.choice(songs)
        
                            print("Now playing:", random_song)
        
                            song_path = os.path.join(music_dir, random_song)
        
                            os.startfile(song_path)
                            input("Press Enter to play another song...")
                    else:
                        print("No music files found in the 'Music' directory.")
                        quit()
      elif'favourite song'in query:
          
          os.startfile('C:\\Users\\laxmi\\Music\\fav.mp3')
          song_duration = 398
          time.sleep(song_duration)
          while True:
                    music_dir = 'Music'
                    songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav', '.ogg', '.flac'))]

                    if songs:
                            random_song = random.choice(songs)
        
                            print("Now playing:", random_song)
        
                            song_path = os.path.join(music_dir, random_song)
        
                            os.startfile(song_path)
                            input("Press Enter to play another song...")
                    else:
                         print("No music files found in the 'Music' directory.")
                         quit()

      elif'time'in query:
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir,The time is {strTime}")

      elif'hello'in query:
          speak("hello sir,nice to meet you")

      elif'what is your name'in query:
          speak("My name is Jarvis.")
          print("My name is Jarvis.")
           
      elif'how are you'in query or'how r u'in query:
          speak("I am fine sir!How are you sir?")
          print("I am fine sir.How are you sir?")
          
      elif'i am fine'in query:
          speak("I am glad to hear that you are doing well!If there is anything else you would like assistance with, feel free to ask.")
          print("I am glad to hear that you are doing well!If there is anything else you would like assistance with, feel free to ask.")
      
      elif'bar' in query:
          webbrowser.open('https://bard.google.com/chat')

      elif'google'in query:
          from search import searchgoogle
          searchgoogle(query)
          break
      elif'go back'in query:
          keyboard.press_and_release('ctrl + w')
          time.sleep(1)
          speak("done sir")
      elif'youtube' in query:
          from search import searchyoutube
          searchyoutube(query)
          
      elif 'exit' in query:
          print(Fore.RED+"Goodbye!")
          speak("Goodbye!")
          break
      elif'good job'in query:
          speak("thanks for your complement sir")
          print("Thanks for your complement sir")
      elif'pause video' in query:
          pyautogui.press("k")
          speak("paused")
      elif'play video'in query or 'play'in query:
          pyautogui.press("Space")
          speak("played")
      elif'stop video'in query or 'stop'in query:
          pyautogui.press("Space")
          speak("stoped")
      elif'mute video'in query:
          pyautogui.press("m")
      elif'full Screen'in query:
          pyautogui.press("f")
      elif'go forward'in query:
          pyautogui.press("l")
      elif'go backward'in query:
          pyautogui.press("j")
      elif'next video'in query:
          keyboard.press_and_release('Shift + n')
      elif'new tab'in query:
          keyboard.press_and_release('ctrl + n')
      elif'continue'in query:
          continue
      elif'open file'in query:
          keyboard.press_and_release('ctrl + o')
      elif'turn on hand control'in query:
          subprocess.run('python', 'Control mouse.py')
      elif'close window'in query:
          keyboard.press_and_release('Alt + F4')
          speak('done sir')
      elif'scroll down'in query or 'down'in query:
          keyboard.press_and_release('Down')
          speak('done sir')
      elif'scroll up'in query or 'up' in query:
          keyboard.press_and_release('Up')
          speak('done sir')
      elif'go right'in query or 'right'in query:
          keyboard.press_and_release('Right')
          speak('done sir')
      elif'go left'in query or 'left'in query:
          keyboard.press_and_release('left')
          speak('done sir')
      else:
           result = wikipedia.summary(query, sentences=3)
           print(result)
           speak(result)
          
          
