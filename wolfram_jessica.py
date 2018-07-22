import config #own
import pyytsx3_jessica as pyt #own
import jessica_words as w
import wolframalpha

App_ID = config.WolframAlpha_ID

def wolf():
	pyt.say("  Wolfram Alpha Module, Ask anythin and see the magic!   ")
	pyt.say("What's the question?")
	x = input("Question: ")
	while (not(set(w.exit_words).intersection(x.split()))):
		try:
			client = wolframalpha.Client(App_ID)
			rest = client.query(x)
			answer = next(rest.results).text
			print (answer)
			pyt.say(answer)
			
			
		except:
			pyt.say("Wrong question.Try again!")
			pyt.say("Ask again")
			x = input("Question: ")






