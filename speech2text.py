import speech_recognition as sr
import sys

class SpeechToText:
    def __init__(self, file=""):
        self.r = sr.Recognizer()
        if (file == ""):
            mic = sr.Microphone()
            with mic as source:
                print("Say something in spanish")
                self.r.adjust_for_ambient_noise(source)
                self.audio = self.r.listen(source)
                print("Listened")
        else:
            src = sr.AudioFile(file)
            with src as source:
                print("Recording audio file")
                self.audio = self.r.record(source)
                print("Recorded")

    def display_audio(self):
        language = raw_input("In wich lenguage is the audio?(English/Spanish) ")

        if language == "Spanish":
            print("Text: " + self.r.recognize_google(self.audio, language="es-ES"))
        else:
            print("Text: " + self.r.recognize_google(self.audio, language="en-EN"))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        StT = SpeechToText(sys.argv[1])
    else:
        stT = SpeechToText()

    stT.display_audio()
