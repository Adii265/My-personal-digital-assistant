import datetime
import calendar

import pyytsx3_jessica as pyt #own
import jessica_words as w



def cal_days(a):
	if a == 0:
		print("MONDAY")
		pyt.say("MONDAY")
	if a == 1:
		print("TUESDAY")
		pyt.say("TUESDAY")
	if a == 2:
		print("WEDNESDAY")
		pyt.say("WEDNSDAY")
	if a == 3:
		print("THURSDAY")
		pyt.say("THRURSDAY")
	if a == 4:
		print("FRIDAY")		
		pyt.say("FRIDAY")
	if a == 5:
		print("SATURDAY")		
		pyt.say("SATURDAY")
	if a == 6:
		print("SUNDAY")
		pyt.say("SUNDAY")




def valid_date(dates):	
	while True:
		
		dd , mm , yy = (int(x) for x in dates.split('-'))
		try:		
			s = datetime.date(yy,mm,dd)
			if s:
				return s	
			else:
				pyt.say("Invalid date, enter again")
				dates = input("DD-MM-YYYY\n")

		except:
			pyt.say("Invalid date, enter again")
			dates = input("DD-MM-YYYY\n")


def day_for_date():
	date= input("Enter date in format (DD-MM-YYYY)\n")
	valid_date(date)
	dd , mm , yy = (int(x) for x in date.split('-'))
	date_spe = datetime.date(yy,mm,dd)
	day_that_date = date_spe.weekday()
	cal_days( day_that_date )


#def work():
#	date= input("Enter date in format (DD/MM/YYYY)\n")
#	while (not(set(w.exit_words).intersection(x.split()))):
#		day_for_date()
#		date= input("Enter date in format (DD/MM/YYYY)\n")




#day_for_date()