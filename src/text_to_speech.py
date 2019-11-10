import pyttsx3


engine = pyttsx3.init()


def say(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
