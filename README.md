# Randall
Open source voice assistant.

## Installing dependencies
Make sure you have Python 3.7.5

Install requirements with pip first.

`pip install -r requirements.txt`

If you're on Windows, `deepspeech==0.5.1` will probably fail to be satisfied. You will have to download the .whl manually from DeepSpeech's releases page on GitHub.
`pyaudio` will probably fail as well. PyAudio for Windows was acquired from `https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio`

Then download package specific datasets.

`python -m spacy download en_core_web_sm`

`nltk.download()` (Choosing all)

`nltk.download('wordnet')`

`wget https://github.com/mozilla/DeepSpeech/releases/download/v0.5.1/deepspeech-0.5.1-models.tar.gz`

## Using the visualizer
`cd ws_echo_server` and `npm i`

Now you can `node index.js` to start the websocket echo server.

Start Randall and navigate to `html/viz.html` on your web browser.