import pyttsx3
import multiprocessing
import os
from src import ws_client


engine = pyttsx3.init()
THREADS = []
print(multiprocessing.current_process().name)


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
