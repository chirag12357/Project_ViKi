##the voice of viki
##this if a funtionn for the text to speech##
import pyttsx3
import pyttsx3
engine = pyttsx3.init()
rate= engine.getProperty('rate')
voices= engine.getProperty('voices')
engine.setProperty('rate',rate-30)
engine.setProperty('voice',voices[2].id)
class main():
    def say(a):
        engine.say(a)
        engine.runAndWait()
