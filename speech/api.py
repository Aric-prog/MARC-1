import speech_recognition as sr
import re
r = sr.Recognizer()

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
            detectKeyword(text)

        except:
            print('Marci could not understand the command')

def listOfWordExistInString(words, text):
    return set(words).intersection(text.split())

def move(orientation, amount):
    print(f"Move {orientation} {amount} cm")

def detectKeyword(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
    if(listOfWordExistInString(['note'], text)):
        # Eat words from the word 'note' to the right
        textContent = text.split('note')[1].strip()
        print("take a note : ", textContent)
    elif(listOfWordExistInString(['go', 'move'], text)):
        orientationList = {
            'forward' : move,
            'back' : move,
            'left' : move,
            'right' : move
        }
        # Find parameters such as the amount you go (1, 5) and direction
        moveAmount = re.search(r'\d+', text).group()
        orientation = ""
        for i in orientationList.keys():
            if(i in text):
                orientation = i
                break
        if(orientation != ""):
            orientationList[orientation](orientation, moveAmount)
        else:
            print("No orientation detected, command denied")
    elif(listOfWordExistInString(['alarm'], text)):
        # PARSE CLOCK :((
        amount = re.search(r'\d+', text).group()
        
        meridiem = ''
        for i in ['am', 'pm']:
            if(i in text):
                meridiem = i
                break
        print(amount, meridiem)
