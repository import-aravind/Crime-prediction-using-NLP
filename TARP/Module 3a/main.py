import smtplib
import speech_recognition as sr
import pyttsx3
import pyaudio
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('emailbottarp@gmail.com', 'Tarp1190Email')
    email = EmailMessage()
    email['From'] = 'emailbottarp@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'COOL_DUDE_EMAIL',
    'Delhi': 'padmamurali2000@gmail.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = input()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = input()
    talk('Tell me the text in your email')
    message = input()
    send_email(receiver, subject, message)
    talk('Your email is sent')
    talk('Do you want to send more email?')
    send_more = input()
    if 'yes' in send_more:
        get_email_info()


get_email_info()