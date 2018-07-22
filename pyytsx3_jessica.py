import pyttsx3

k = pyttsx3.init()
#rate = k.getProperty('rate')
#print(rate)
k.setProperty('voice', 'english+f1')
k.setProperty('rate', 160)
def say(text):
	k.say(text)
	k.runAndWait()

#say("MY name is Aditi")