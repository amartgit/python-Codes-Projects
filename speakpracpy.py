import pyttsx3

print("Welcome to Robo speaker")
text_speech = pyttsx3.init()

while True:
    x = input("Enter what you want to say:")
    text_speech.say(x)
    text_speech.runAndWait()
    if x == "q":
        text_speech.say("Bye bye for now, dear friend")
        text_speech.runAndWait()
        break
