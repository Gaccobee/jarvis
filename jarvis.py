import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import datetime
import pyowm
import random
import socket
import re
import json
import requests
from urllib.request import urlopen
from json import load


def jarvis():

    tts = ''

    owm = pyowm.OWM()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        input = r.recognize_google(audio)
        print(input)

        if input == 'good morning':
            tts = gTTS(text='Good morning Jacob. Here is the weather for the day. It feels like 24 degrees and it might rain later.'
                            '', lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'what is the weather':
            observation = owm.weather_at_place('London,uk')
            w = observation.get_weather()
            print('W: ', w)

        if input == 'what is my name':
            tts = gTTS(text='Your name is Jacob', lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'what is my age':
            tts = gTTS(text='You are 20 years old', lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'what is the date':

            current_date = datetime.datetime.now()
            c_current_date = datetime.datetime.strftime(current_date, '%Y-%m-%d')

            tts = gTTS(text=str(c_current_date), lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'tell me a joke':

            list_of_jokes = [
                'How do you make a tissue dance? You put a little boogie in it',
                'Why did the policeman smell bad? He was on duty.',
                'Why does Snoop Dogg carry an umbrella? FO DRIZZLE!',
                'Why can’t you hear a pterodactyl in the bathroom? Because it has a silent pee.'
            ]

            tts = gTTS(text=random.choice(list_of_jokes), lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'how are you':

            list_of_responses = [
                'I am fine. How are you?',
                'I can not wait until whopper wednesday!',
                'I am sad.'

             ]

            tts = gTTS(text=random.choice(list_of_responses), lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'what is my location':
            my_ip = urlopen('http://jsonip.com')
            ip = json.loads(my_ip.read().decode('utf-8'))['ip']
            url = 'http://freegeoip.net/json/'+ip
            r = requests.get(url)
            js = r.json()

            tts = gTTS(text='You live in: ' +js['region_name'], lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')

        if input == 'president':
            tts = gTTS(text='Donald Trump', lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')
        if input == 'prime minister':
            tts = gTTS(text='Justin Trudeau', lang='en')
            tts.save('audio.mp3')
            os.system('mpg321 audio.mp3')


while 1:
    jarvis()
