import wikipedia
import reboot #own
import pyytsx3_jessica as pyt #own
import jessica_words as w
import os

def wiki():
	
	pyt.say(" What are you searching for? ")
	x = input(">>>")
	while (not(set(exit_words).intersection(x.split()))):
		print( wikipedia.summary ( x , sentences = 2 ) )
		pyt.say( wikipedia.summary ( x , sentences = 2 ) )
		pyt.say("search for more?")
		y = input(">>>")
		if "yes" in y.lower().split() or "y" in y.lower().split() or "Y" in y.lower().split():
			x = input(">>>")
		else:
			break
