import pyttsx3
import multiprocessing
from randall import ws_client

THREADS = []
engine = pyttsx3.init()


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
    ws_client.send_start()
    print(text)
    engine.say(text)
    engine.runAndWait()
    ws_client.send_stop()
