from googletrans import Translator  # Import Translator module from googletrans package
from say import *
translator = Translator() # Create object of Translator.
translated = translator.translate('fuck', dest='ja')
print(translated.text)
a=translated.pronunciation
main.say(a)
print(a)
