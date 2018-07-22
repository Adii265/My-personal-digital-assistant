import os
from datetime import datetime
from datetime import date
from datetime import time
import time
import calendar
import sys
import datetime

import reboot #own
import pyytsx3_jessica as pyt #own



exit_words = ["thanks","thanku","back","end","exit","thank","quit","Quit","Thanks","Thanku","Back","End","Exit","Thank"]
def cal():
	print (" Searching for \n Current month \n Calendar of specific month \n Calendar of specific year \n Leapyear \n If yes, then say it!.\n")
	pyt.say( " Searching for Current month calendar of specific month and year calendar of specific year leapyear, If yes, then say it.")
	x = input(">>>")
	while (not(set(exit_words).intersection(x.split()))):
		

		#To print the calendar of current month
		if "this month" in x or "current month" in x or "This month" in x or "Current month" in x or "Calendar of this month" in x or "calendar of this month" in x:
			now = datetime.datetime.now() 
			mm = now.month			
			yy = now.year
			print(calendar.month(yy,mm))	
			x = input(">>>")


		#To print the calendar of a specific month and year
		elif "Calendar of month " in x or "calendar of month" in x or "specific month" in x or "Specific month" in x or "month" in x.split() or "Month" in x.split():
			yy = int(input("Year?"))
			mm = int(input("month"))
			print(calendar.month(yy,mm))	
			x = input(">>>")
		
		
		#To print the calendar of a specific year
		elif "Calendar of specific year" in x or "calendar of specific year" in x or "specific year" in x or "Specific year" in x:
			yy = int(input("Year?"))
			print(calendar.calendar(yy))		
			x = input(">>>")

	
		#To check a leap year
		elif "leapyear" in x.split():
			yy = int(input("year?"))
			pyt.say(calendar.isleap(yy))
			x = input(">>>")


		#if words do not match
		else:
			pyt.say("Not understood! Please say again.")
			x = input(">>>")
	



#Function for today's date
def today_date():
	pyt.say("Today's date is:")
	today = date.today()
	pyt.say(today)
	print(today)



#def current_time():
#	pyt.say("The time is:")
#	time1 = datetime.now()
#	pyt.say(time1.strftime("%X"))
#	print(time1.strftime("%X"))






