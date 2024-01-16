from email import message
import os
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from emailcredentials import sender_email, email_password, receiver_email
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient 
import clipboard
import pyjokes
import string
import random
import io

engine = pyttsx3.init()
voices = 1

def spironSpeak(audio):
    engine.say(audio)
    engine.runAndWait()

def getVoices(voices):
    voices = engine.getProperty("voices")
    if(voices == 1):
        engine.setProperty("voice", voices[0].id)
        spironSpeak("Spy ron at your service.")
    if(voices == 2):
        engine.setProperty("voice", voices[1].id)
        spironSpeak("Saturday at your service.")

def getTime():
    time = datetime.datetime.now().strftime("%I:%M")
    spironSpeak(f"The current time is: {time}")

def getDate():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    spironSpeak(f"The Current Date is {month} {day} {year}")

def greetMe():
    hour = datetime.datetime.now().hour
    if(hour >= 6 and hour < 12):
        spironSpeak("Good Morning Sir")
    elif(hour >= 12 and hour < 18):
        spironSpeak("Good Afternoon Sir")
    elif(hour >= 18 and hour < 24):
        spironSpeak("Good Evening Sir")
    else:
        spironSpeak("Good Night Sir")
    spironSpeak("How can I help you? ")

def wishMe():
    spironSpeak(greetMe())
    getTime()
    getDate()
    spironSpeak("How can I help you today!")

def takeCommandCMD():
    query = input("How can I help you? \n")
    return query

def takeCommandMIC():
    recognize = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        print("I'm Listening...")
        recognize.pause_threshold = 1
        audio = recognize.listen(source)
    try: 
        print("Computing...")
        query = recognize.recognize_google(audio, language = "en-US")
        print(query)
    except Exception as error:
        print(error)
        spironSpeak("Sorry, I Couldn't Hear You! Say It Again Please...")
        return "None"
    return query

def sendEmail(receiver, subject_line, email_content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, email_password)
    email = EmailMessage()
    email["From"] = sender_email
    email["To"] = receiver
    email["Subject"] = subject_line
    email.set_content(email_content)
    server.send_message(email)
    server.close()

def searchGoogle():
    spironSpeak("What Do You Want Me to search")
    search = takeCommandMIC()
    wb.open('https:/www.google.com/search?q='+search)

def newsUpdate():
    newsapi = NewsApiClient(api_key = '98d6f8ed271e49eab6c00bb29b797571')
    spironSpeak("What Topic do you want news on?")
    print("What Topic do you want news on?")
    user_news_request = takeCommandMIC()

    data = newsapi.get_top_headlines(q = user_news_request,
                                    language = 'en',
                                    page_size = 5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{y["description"]}')
        spironSpeak(f'{y["description"]}')
    spironSpeak(f"That is all the news regarding {user_news_request} for now.")
    print(f"That is all the news regarding {user_news_request} for now!")

def textReader():
    text = clipboard.paste()
    print(text)
    spironSpeak(text)

def covidUpdate():
    url = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data = url.json()
    covid_data = (f"There have been {data['cases']} active cases, {data['deaths']} deaths, and {data['recovered']} recovered cases")
    spironSpeak(covid_data)
    print(covid_data)

def screenShot():
    image_name = str(datetime.datetime.now())
    image_name = image_name.replace(":", "_")
    #image_name = f'C:\\Automation\\screenshots\\{image_name}.png'
    image_name = f'.\\screenshots\\{image_name}.png'
    image = pyautogui.screenshot(image_name)
    image.show()

def passwordGenerator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    pass_length = 12
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    new_pass = ("".join(s[0:pass_length]))
    print(new_pass)
    spironSpeak(new_pass)

def logFile():
    log_name = str(datetime.datetime.now())
    log_name = log_name.replace(":", "_")
    spironSpeak("Log Recording Active...")
    log_content = takeCommandMIC()
    log_write = open(f'C:\Automation\Journal Files\\{log_name}', 'w')
    log_write.write(log_content)
    log_write.close()

def songChoice():
    spironSpeak("What song do you want to play?")
    print("What song do you want to play?")
    song_request = takeCommandMIC().lower()
    
    if('1600 rated player' in song_request):
        song_path = 'C:\Automation\project songs\\161660.mp4'
        os.startfile(song_path)
        quit()

    if('ant-man' in song_request or 'thief' in song_request):
        song_path = 'C:\Automation\project songs\\antman_theme.mp4'
        os.startfile(song_path)
        quit()

    if('back in black' in song_request or 'iron man' in song_request):
        song_path = 'C:\Automation\project songs\\back_in_black.mp4'
        os.startfile(song_path)
        quit()

    if('believer' in song_request):
        song_path = 'C:\Automation\project songs\\believer.mp4'
        os.startfile(song_path)
        quit()
    
    if('black widow' in song_request):
        song_path = 'C:\Automation\project songs\\black_widow_opening.mp4'
        os.startfile(song_path)
        quit()

    if('avenger' in song_request):
        song_path = 'C:\Automation\project songs\\bring_me_thanos.mp4'
        os.startfile(song_path)
        quit()

    if('bulletproof' in song_request):
        song_path = 'C:\Automation\project songs\\bulletproof.mp4'
        os.startfile(song_path)
        quit()
    
    if('60s spiderman' in song_request or 'back in time' in song_request):
        song_path = 'C:\Automation\project songs\\classic_spiderman.mp4'
        os.startfile(song_path)
        quit()

    if('come and get your love' in song_request or 'infinity stone' in song_request):
        song_path = 'C:\Automation\project songs\\come_and_get_your_love.mp4'
        os.startfile(song_path)
        quit()

    if('darkside' in song_request  or 'sociopath' in song_request):
        song_path = 'C:\Automation\project songs\\darkside.mp4'
        os.startfile(song_path)
        quit()
    
    if('fight back' in song_request):
        song_path = 'C:\Automation\project songs\\fight_back.mp4'
        os.startfile(song_path)
        quit()
    
    if('glory' in song_request):
        song_path = 'C:\Automation\project songs\\glory.mp4'
        os.startfile(song_path)
        quit()
    
    if('guardian' in song_request):
        song_path = 'C:\Automation\project songs\\guardians_theme.mp4'
        os.startfile(song_path)
        quit()

    if('highway to hell' in song_request or 'inventor' in song_request):
        song_path = 'C:\Automation\project songs\\highway_to_hell.mp4'
        os.startfile(song_path)
        quit()

    if('kai theme' in song_request or 'kung fu' in song_request):
        song_path = 'C:\Automation\project songs\\kai_theme.mp4'
        os.startfile(song_path)
        quit()

    if('killmonger theme' in song_request or 'wankandan' in song_request):
        song_path = 'C:\Automation\project songs\\killmonger_theme.mp4'
        os.startfile(song_path)
        quit()

    if('mandalorian' in song_request or 'bounty hunter' in song_request):
        song_path = 'C:\Automation\project songs\\mando.mp4'
        os.startfile(song_path)
        quit()

    if('hikaru' in song_request or 'grand' in song_request):
        song_path = 'C:\Automation\project songs\\mate_in_one.mp4'
        os.startfile(song_path)
        quit()

    if('mightiest' in song_request or 'mighty' in song_request):
        song_path = 'C:\Automation\project songs\\mightiest_heroes.mp4'
        os.startfile(song_path)
        quit()

    if('miracle' in song_request):
        song_path = 'C:\Automation\project songs\\miracle.mp4'
        os.startfile(song_path)
        quit()

    if('strings' in song_request or 'ultron' in song_request):
        song_path = 'C:\Automation\project sogns\\no_strings_on_me.mp4'
        os.startfile(song_path)
        quit()

    if('steve' in song_request or 'death' in song_request):
        song_path = 'C:\Automation\project ssongs\\oh_death.mp4'
        os.startfile(song_path)
        quit()

    if('lonliest' in song_request):
        song_path = 'C:\Automation\project songs\\one_is_the_lonliest_number.mp4'
        os.startfile(song_path)
        quit()

    if('payback' in song_request or 'deckard' in song_request or "shaw" in song_request):
        song_path = 'C:\Automation\project songs\\payback.mp4'
        os.startfile(song_path)
        quit()

    if('pirate' in song_request):
        song_path = 'C:\Automation\project songs\\pirates_of_the_caribbean.mp4'
        os.startfile(song_path)
        quit()

    if('portal' in song_request):
        song_path = 'C:\Automation\project songs\\portals_scene.mp4'
        os.startfile(song_path)
        quit()

    if('ragnorok' in song_request or 'thor' in song_request):
        song_path = 'C:\Automation\project songs\\ragnorok.mp4'
        os.startfile(song_path)
        quit()

    if('requiem' in song_request or 'dreaam' in song_request):
        song_path = 'C:\Automation\project songs\\requiem_for_a_dream.mp4'
        os.startfile(song_path)
        quit()

    if('rise' in song_request):
        song_path = 'C:\Automation\project songs\\rise.mp4'
        os.startfile(song_path)
        quit()

    if('rook' in song_request or 'gotham' in song_request):
        song_path = 'C:\Automation\project songs\\rook_a4.mp4'
        os.startfile(song_path)
        quit()

    if('run it' in song_request):
        song_path = 'C:\Automation\project songs\\run_it.mp4'
        os.startfile(song_path)
        quit()

    if('sad song' in song_request or 'see you again' in song_request):
        song_path = 'C:\Automation\project songs\\see_you_again.mp4'
        os.startfile(song_path)
        quit()

    if('shang' in song_request):
        song_path = 'C:\Automation\project songs\\shang_chi_trailer.mp4'
        os.startfile(song_path)
        quit()

    if('spectacular' in song_request):
        song_path = 'C:\Automation\project songs\\spectacular_spiderman.mp4'
        os.startfile(song_path)
        quit()

    if('stronger' in song_request):
        song_path = 'C:\Automation\project songs\\stronger.mp4'
        os.startfile(song_path)
        quit()

    if('tetris' in song_request):
        song_path = 'C:\Automation\project songs\\tetris.mp4'
        os.startfile(song_path)
        quit()

    if('chain' in song_request):
        song_path = 'C:\Automation\project songs\\the_chain.mp4'
        os.startfile(song_path)
        quit()

    if('uptown' in song_request):
        song_path = 'C:\Automation\project songs\\uptown_funk.mp4'
        os.startfile(song_path)
        quit()

    if('venom' in song_request):
        song_path = 'C:\Automation\project songs\\venom.mp4'
        os.startfile(song_path)
        quit()

    if('warriors' in song_request):
        song_path = 'C:\Automation\project songs\\warriors.mp4'
        os.startfile(song_path)
        quit()

    if('fast' in song_request or 'we own it' in song_request):
        song_path = 'C:\Automation\project songs\\we_own_it.mp4'
        os.startfile(song_path)
        quit()

if __name__ == "__main__":
    greetMe()
    while(True):
        query = takeCommandMIC().lower()
        if("time" in query):
            getTime()
        elif ("covid" in query):
            covidUpdate()
        elif("date" in query):
            getDate()
        elif ("email" in query):
            email_list = {
                "Zachary": 'zach.trapani@gmail.com',
                "Samuel": 'papoa479@gmail.com',
                "Halo": 'paolo.serrato1013@gmail.com',
                "test": 'SuperiorSpiron1@gmail.com',
                "turn off": 'Pranav.lee.bonagiri@gmail.com'
            }
            try:
                spironSpeak("Who Do you Want to Send an Email?")
                print("Who Do you Want to Send an Email?")
                receiver_name = takeCommandMIC()
                receiver = email_list[receiver_name]
                spironSpeak("What Would You Like For Your Subject?")
                print("What Would You Like For Your Subject?")
                subject = takeCommandMIC()
                spironSpeak("What Do You Want Your Email To Say? ")
                email_content = takeCommandMIC()
                sendEmail(receiver, subject, email_content)
                spironSpeak("Email Has Been Sent")
                print("Your Email Has Been Sent!")
            except Exception as e:
                print(e)
                spironSpeak("Unable to Send The Email")

        elif("journal" in query or "log" in query):
            logFile()

        elif ("wikipedia" in query):
            try:
                spironSpeak("I'm Searching...")
                print("I'm Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                spironSpeak(result)
            except Exception as e:
                print(e)
                spironSpeak("Unable to Find a Result!")
                print("Unable to find a Result!")

        elif ("youtube" in query):
            spironSpeak("What Video Do You Want to watch?")
            print("\nWhat Video Do You Want To Watch?")
            video_topic = takeCommandMIC()
            pywhatkit.playonyt(video_topic)
            break 
        
        elif ("google" in query):
            searchGoogle()
        
        elif ("play my favorite song" in query):
            rick_roll_directory = "D:\\project songs\\rickroll.mp4"
            os.startfile(rick_roll_directory)
            break
        
        elif ("weather" in query):
            try:
                spironSpeak("Which city or state weather information do you want?")
                print("Which city or state weather information do you want?")
                location = takeCommandMIC()
                url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&units=imperial&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd'
                res = requests.get(url)
                data = res.json()
                weather = data['weather'] [0] ['main']
                temperature = data['main']['temp']
                temperature_celcius = round((temperature - 32) * 5/9)
                description = data['weather'][0]['description']
                print(weather)
                print(temperature)
                print(temperature_celcius)
                print(description)
                spironSpeak(f"The Temperature of {location} is {temperature} degrees Farenheit, {temperature_celcius} degrees Celcius, and it's described to have {description}")
            except Exception as e:
                print(e)
                spironSpeak("Unable to find location!")
                print("Unable to find a location!")

        elif ("coordinate" in query):
            try:
                spironSpeak("What location do you want to find coordinates for?")
                print("Which location do you want to find coordinates for?")
                location = takeCommandMIC()
                url = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&units=imperial&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd'
                res = requests.get(url)
                data = res.json()
                coordinates_lat = data['coord']['lat']
                coordinates_long = data['coord']['lon']
                print(coordinates_lat, coordinates_long)
                spironSpeak(f"{location} is located at {coordinates_lat} latitude and {coordinates_long} longitude")
            except Exception as e:
                print(e)
                spironSpeak("Unable to find Location!")
                print("Unable to Find Location!")

        elif ("news" in query):
            newsUpdate()

        elif ("read" in query):
            textReader()

        elif ("software" in query):
            spironSpeak("What Software do you want to open?")
            print("What software do you want to open?")
            software_request = takeCommandMIC().lower()
            if(software_request == "visual code"):
                codepath = 'C:\Program Files\Microsoft VS Code\Code.exe'
            elif(software_request == "blender"):
                codepath = 'C:\Program Files\Blender Foundation\Blender 2.93\\blender.exe'
            elif(software_request == "discord"):
                codepath = 'C:\Program Files\Discord\Discord.exe'
            elif(software_request == "photoshop"):
                codepath = 'C:\Program Files\Adobe Photoshop CS6\Adobe Photoshop CS6\Photoshop.exe'

            os.startfile(codepath)

        elif ("open" in query):
            os.system('explorer :\\{}'.format(query.replace('Open','')))

        elif("joke" in query):
            # random_joke = pyjokes.get_jokes()[random.randint(0,100)]
            random_joke = pyjokes.get_jokes()
            random_joke = random.choice(random_joke)
            print("\n\n")
            print(random_joke)
            spironSpeak(random_joke)

        elif("screenshot" in query):
            screenShot()

        elif("remember" in query):
            spironSpeak("What should I remember?")
            print("What should I remember?")
            remember_request = takeCommandMIC()
            remember_request.replace("I", "You")
            spironSpeak("Alright, I will remember that" + remember_request)
            remember = open('remember_data.txt', 'w')
            remember.write(remember_request)
            remember.close()

        elif("tell you" in query):
            remember = open('remember_data.txt', 'r')
            spironSpeak("You told me to remember that" + remember.read())

        elif('password' in query):
            passwordGenerator()

        elif('song' in query):
            songChoice()

        elif("quit" in query or "shut down" in query or "shutdown" in query):
            spironSpeak("Okay, Shutting Down! Have A good Day!")
            break
        else:
            spironSpeak("I'm not quite sure how to respond to that")


