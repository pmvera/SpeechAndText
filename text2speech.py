from gtts import gTTS
import sys
import os

class TextToSpeech:
    def __init__(self):
        text = raw_input("Write your text: ")

        audio = gTTS(text=text, lang=sys.argv[1], slow=False)
        audio.save(sys.argv[2])

        os.system("mpg321 " + sys.argv[2])
        os.remove(sys.argv[2])

if __name__ == '__main__':
    if len(sys.argv) == 3:
        TtS = TextToSpeech()
    else:
        print("python program_name language audio-file_name")
