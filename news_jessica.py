import pyytsx3_jessica as pyt #own
import reboot #own
import config #own

import json
import requests
import jessica_words as w



def newss(url):
	open_page = requests.get(url).json()
	article = open_page["articles"]
	results = []
     
	for ar in article:
	        results.append(str(ar["title"]))
         
	for i in range(len(results)):
		print(i + 1, results[i])
		pyt.say(results[i])          





def speak_news():

	pyt.say(" 1 National News. or 2 International News. \n")
	print("\n 1.National News \n 2.International News \n") 
	x = input(">>>")
	

	if "National" in x.lower().split() or "national" in x.lower().split():
		print("\n1.1.Headlines  \n 1.2.Sports \n 1.3.Buisness \n")
		x = input(">>>")
		if "headlines" in x.lower().split() or "highlights" in x.lower().split() or "todays_news" in x.lower().split():
			url = config.Times_Of_India
			newss(url)
		

		elif "sports" in x.lower().split() or "Sports" in x.lower().split():
			url = config.BBC_sports_news	
			newss(url)


		elif "buisness" in x.lower().split() or "Buisness" in x.lower().split():
			url = config.Financial_Time
			newss(url)





	elif "International" in x.lower().split() or "international" in x.lower().split():
		print("\n 1.USA \n 2.UK\n")
		x = input(">>>")
		if "usa" in x.lower().split() or "USA" in x.lower().split():
			url = config.USA_Today
			newss(url)
		elif "uk" in x.lower().split() or "UK" in x.lower().split():
			url = config.Buisness_Insider_UK
			newss(url)

	#elif w.exit_words in x.split():
		exit(0)


	else:
		pyt.say("Exiting module")


#speak_news()