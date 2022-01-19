from itsdangerous import json
import speech_recognition as sr
import re
from flask import Flask
from flask import Blueprint

app = Flask(__name__)

# TODO : Initialize flask server here with their endpoints, also find out how to do http request to the other sockets 
r = sr.Recognizer()
bp = Blueprint("speech", __name__, url_prefix="/speech")

@bp.route("/listen")
def startListening():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Marci is now listening')
        audio = r.listen(source)
        
        try:
            # Separate intent and parameter
            # Get keywords like go, move, set alarm,
            text = r.recognize_google(audio)
            print("Recognized voice input : ", text)
            return detectKeyword(text)

        except:
            print('Marci could not understand the command')

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
            'back',
            'left',
            'right' 
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

        if(orientation != ''):
            return 401
    elif(listOfWordExistInString(['alarm'], text)):
        # PARSE CLOCK :((
        time = re.search(r'\d+', text).group()
        meridiem = ''

        for i in ['am', 'pm']:
            if(i in text):
                meridiem = i
                break

        response['event'] = 'alarm'
        response['meridiem'] = meridiem
        response['time'] = time
    print(response)
    return json.dumps(response, indent = 4)

if __name__ == '__main__':
    app.register_blueprint(bp)
    app.run(port=8002, host='localhost')