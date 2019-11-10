import pyttsx3
import multiprocessing


engine = pyttsx3.init()
THREADS = []


def say(text):
    global THREADS
    thread = multiprocessing.Process(target=do, args=(text,))
    thread.start()
    THREADS.append(thread)


def kill():
    global THREADS
    for thread in THREADS:
        thread.terminate()
    THREADS = []


def do(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
