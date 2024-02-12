import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("Welcome to Robo Speaker 1.1 created by Aarushi")
engine.say("Welcome to Robo Speaker 1.1 created by Aarushi!")
engine.runAndWait()

while True:
    x = input("Enter what you want me to speak (type 'q' to quit): ")
    if x == "q":
        engine.say("goodbye")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()

print("Goodbye!")
engine.stop()
