import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Devanshu")
    while True:
        x = input("Enter what do you want me to pronounce: ")
        if x=='q':
            os.system(f'mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""Bye Bye dev "")(window.close)")')
            break
        command =f'mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{x}"")(window.close)")'
        os.system(command) #automatically runs the command
