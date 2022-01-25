from itsdangerous import json
import speech_recognition as sr
import requests
import alarm
import re
from flask import Flask, Response
from flask import Blueprint

app = Flask(__name__)

# TODO : Initialize flask server here with their endpoints, also find out how to do http request to the other sockets 
r = sr.Recognizer()
bp = Blueprint("speech", __name__, url_prefix="/")

@bp.route("/listen")
def acceptListenRequest():
    # Turns out requests only resolve after after_request
    try:
        with sr.Microphone() as source:
            print('Marci is now listening')
            requests.post('http://localhost:8000/listenStatus')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print("Recognized voice input : ", text)
            detectedEvent = detectKeyword(text)
            if('event' in detectedEvent):
                return detectedEvent
            else:
                return Response(status=401)
    except sr.UnknownValueError:
        print("Marci couldn't understand what you said")
        return Response(status=401)

def listOfWordExistInString(words, text):
    return set(words).intersection(text.split())

# TODO : replace this with actual move amount
def move(orientation, amount):
    print(f"Move {orientation} {amount} cm")

def detectKeyword(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9 \n]', '', text)

    response = {}
    if(listOfWordExistInString(['note'], text)):
        # Eat words from the word 'note' to the right
        textContent = text.split('note')[1].strip()
        response['event'] = 'note'
        response['content'] = textContent
    elif(listOfWordExistInString(['go', 'move'], text)):
        orientationList = [
            'forward',
            'reverse',
            'left',
            'right', 
        ]
        # Find parameters such as the amount you go (1, 5) and direction
        moveAmount = re.search(r'\d+', text).group()
        orientation = "forward"
         
        for i in orientationList:
            if(i in text):
                orientation = i
                break

        response['event'] = 'move'
        response['orientation'] = orientation
        response['moveAmount'] = moveAmount
    elif(listOfWordExistInString(['alarm'], text)):
        # PARSE CLOCK :((
        # Let's just do military time :))
        time = re.search(r'\d+', text).group()
    
        response['event'] = 'alarm'
        response['time'] = time
        alarm.alarm(time)
    
    # Response json is for internal use 
    # Send this straight to central module
    return response

# This app should run on port 8002
app.register_blueprint(bp)