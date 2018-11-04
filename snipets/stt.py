

# NOTE: this example requires PyAudio because it uses the Microphone class
from say import *

import speech_recognition as sr
class stt:
    def listen(audio):
# obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

         #recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            b=r.recognize_google(audio)
            print(b)
            main.say(b)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
##    WIT_AI_KEY = "L7YULIZTSFDPUK4BM2HWPV2Y7PZMYDAS"  # Wit.ai keys are 32-character uppercase alphanumeric strings
##    try:
##        print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
##    except sr.UnknownValueError:
##       print("Wit.ai could not understand audio")
##    except sr.RequestError as e:
##        print("Could not request results from Wit.ai service; {0}".format(e))
##        # recognize speech using Houndify
##    HOUNDIFY_CLIENT_ID = "7o44Vz9xqGuM5dsADls3jw=="  # Houndify client IDs are Base64-encoded strings
##    HOUNDIFY_CLIENT_KEY = "NkPzEFYxfuVP6HQ_FXzQmUWy_YsMbukW-QFp-nvffMjnnsh72-9t6FrpJc8Jf9hvmJp-l_LEbIj1_iCKQo7hPw=="  # Houndify client keys are Base64-encoded strings
##    try:
##        print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
##    except sr.UnknownValueError:
##        print("Houndify could not understand audio")
##    except sr.RequestError as e:
##        print("Could not request results from Houndify service; {0}".format(e))
##
##
