from ast import Return
from itsdangerous import json
import speech_recognition as sr
import requests
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
    with sr.Microphone() as source:
        print('Marci is now listening')
        requests.post('http://localhost:8000/listenStatus')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Recognized voice input : ", text)
            detectedEvent = detectKeyword(text)
            if('event' in detectedEvent):
                # requests.post()
                return Response(status=201)
                # Do stuff and send this to central
            else:
                return Response(status=401)
        except:
            print('Marci could not understand the command')
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
        orientation = ""
         
        for i in orientationList.keys():
            if(i in text):
                orientation = i
                break

        response['event'] = 'move'
        response['orientation'] = orientation
        response['moveAmount'] = moveAmount

        if(orientation == ''):
            response['statusCode'] = 401
    elif(listOfWordExistInString(['alarm'], text)):
        # PARSE CLOCK :((
        # Let's just do military time :))
        time = re.search(r'\d+', text).group()
    
        response['event'] = 'alarm'
        response['time'] = time
    
    # Response json is for internal use 
    # Send this straight to central module
    return response

# This app should run on port 8002
app.register_blueprint(bp)