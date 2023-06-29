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
'''
If you want to use Powershell instead of command promt use
        command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\\"{x}\\");"'

If you are not using windows os-

    For mac update the command to
         command = f'say "{x}"'

    For ubuntu
        command = f'spd-say "{x}"'

'''
