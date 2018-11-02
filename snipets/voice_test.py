import pyttsx3
engine = pyttsx3.init()
rate= engine.getProperty('rate')
voices= engine.getProperty('voices')
engine.setProperty('rate',rate-50)
engine.setProperty('voice',voices[2].id)
engine.say("""hey my name is viki
i am your digital friend and will assist you in any way you want me to
just call me and i'll be here
listening""")
engine.runAndWait()

