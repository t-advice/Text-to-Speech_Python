import pyttsx3

engine = pyttsx3.init()

text_to_speech = "Hello World, the automation system is ready."
engine.say(text_to_speech)
engine.runAndWait()


