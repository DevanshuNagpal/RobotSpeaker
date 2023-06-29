import os


if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Devanshu")
    while True:
        x = input("Enter what do you want me to pronounce: ")
        if x=='q':
            os.system(f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\\"Bye Bye Dev\\");"')
            break
        command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\\"{x}\\");"'
        os.system(command) #automatically runs the command
