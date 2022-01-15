import speech_recognition as sr

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
            print(f"Output : {text}")
        except:
            print('Marci could not understand the command')
    