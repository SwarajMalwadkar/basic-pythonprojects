import os
import win32com.client as wincom

speak = wincom.Dispatch("sapi.SpVoice")

if __name__== '__main__':
    while True:
        print("welcome to robo speaker")
        x=input("enter what you want me to pronounce :")
        if x == "quit":
            break
        speak.Speak(x)