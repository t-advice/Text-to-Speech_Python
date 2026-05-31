import pyttsx3

engine = pyttsx3.init()

text_to_speech = "Hello World, the automation system is ready."
engine.say(text_to_speech) # Pass the text to be spoken to the say() method of the engine object. This method queues the text for speech synthesis.
engine.runAndWait()


