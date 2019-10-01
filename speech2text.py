import speech_recognition as sr
import sys

class SpeechToText:
    def __init__(self, file=""):
        r = sr.Recognizer()
        if (file == ""):
            mic = sr.Microphone()
            with mic as source:
                print("Say something in spanish")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                print("Listened")
        else:
            src = sr.AudioFile(file)
            with src as source:
                print("Recording audio file")
                audio = r.record(source)
                print("Recorded")


            print("Text: " + r.recognize_google(audio, language="es-ES"))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        StT = SpeechToText(sys.argv[1])
    else:
        stT = SpeechToText()
