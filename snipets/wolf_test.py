import wolframalpha
from say import *
class wolfi():
    def wolf(a):
        app_id = "5GEP5E-WLH68H46PA"
        client= wolframalpha.Client(app_id)
        a=input("question : ")
        res=client.query(a)
        b=next(res.results).text
        engine.say(b)

