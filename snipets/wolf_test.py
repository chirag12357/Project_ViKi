import wolframalpha
import speech_recognition as sr
from say import *
class wolfi():
    def wolf(b):
        app_id = "5GEP5E-WLH68H46PA"
        client= wolframalpha.Client(app_id)
        res=client.query(b)
        a=next(res.results).text
        main.say(a)

