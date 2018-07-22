import pyytsx3_jessica as pyt #own


import datetime
from datetime import date
from datetime import datetime
from datetime import time





def schedule():
	file_name = "reminder_jessica.txt"
	todays = date.today()
	#print(todays)
	dates = str(todays)
	f = open(file_name,"r")
	flag = 0
	for line in f:
		if dates in line:
			#print (line)
			#pyt.say(line)
			flag = flag + 1

	#print(flag)
		
	if flag: 
		pyt.say("Reminder exists.If you want to read it press Y/y")
		print("Reminder exists.If you want to read it press Y/y")
		ans = input(">>>")
		if ans == 'Y' or ans == "y" or ans == "Yes" or ans == "yes":
			print (line)
			pyt.say(line)

		else:
			pyt.say("Ookay")

	f.close()


#schedule()