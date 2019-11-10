def main():
    parser = argparse.ArgumentParser(description='Stream from microphone using VAD')
    parser.add_argument('-m', '--model', required=True,
                        help='Path to the model (protocol buffer binary file, or entire directory containing all standard-named files for model)')
    args = parser.parse_args()
    stt_settings = {
      'alphabet': 'alphabet.txt',
      'beam_width': 500,
      'device': None,
      'lm': 'lm.binary',
      'lm_alpha': 0.75,
      'lm_beta': 1.85,
      'model': args.model,
      'n_context': 9,
      'n_features': 26,
      'nospinner': False,
      'rate': 16000,
      'savewav': None,
      'trie': 'trie',
      'vad_aggressiveness': 3
    }
    stt.init(SimpleNamespace(**stt_settings), on_speech)
    tts.init()
    # natty.text_to_token("hey oracle, what time is it in manhattan")


def on_speech(text):
    print("Recognized: %s" % text)
    natty.text_to_token(text)


if __name__ == '__main__':
    from src import natural_language_processing as natty
    from src import speech_to_text as stt
    from src import text_to_speech as tts
    from types import SimpleNamespace
    import argparse
    import multiprocessing

    multiprocessing.set_start_method('spawn')
    main()