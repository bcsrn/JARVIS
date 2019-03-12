from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import sys

def talkToMe(audio):
    print(audio)    
    tts = gTTS(text = audio, lang = 'en')
    tts.save('Audio.mp3')
    os.system('Audio.mp3')
    
#listens for commands
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')       
#loop back to continue to listen for commands
    except sr.UnknownValueError:
        assistant(myCommand())
        
    return command
#if statements for executing commands
def assistant(command):    
    if 'open Reddit' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        chrome = webbrowser.get(chrome_path)
        chrome.open('http://google.com')
        chrome.open_new_tab('http://reddit.com')
        
    if 'what\'s up' in command:
        talkToMe('just doing my thing')

    if 'how are you' in command:
        talkToMe('fine, thankyou')
        
    if 'email' in command:
        talkToMe('who is the receipient')
        receipient = myCommand()

        if 'john' is receipient:
            talkToMe('what should I say')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encript our session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('persons name', 'email adress', content)

            #close mail connection
            mail.close()

            talkToMe('email sent')

    if 'exit' in command:
        sys.exit()      


talkToMe('I am ready for your command')
while True:    
    assistant(myCommand())
                        
