import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
voice = engine.getProperty('voices')
volume = engine.getProperty('volume')

engine.setProperty('rate', 200)
engine.setProperty('voices', voice[0].id)
engine.setProperty('volume', 1.0)

def speak(audio):    #voice
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    record = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        record.pause_threshold = 1
        audio = record.listen(source)
    try:
        print("Recognizing...")
        query = record.recognize_google(audio, language='en-in')
        print(query)
        return query
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

def give_task(self):
	data = takeCommand()
	remember = open('order.txt','w')
	remember.write(data)
	remember.close()