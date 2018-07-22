import os
from datetime import datetime
from datetime import date
from datetime import time
from datetime import datetime
import time
import calendar
import sys
import datetime

import reboot #own
import pyytsx3_jessica #own
import jessica_words as w

reminder_path = "Dairy.txt"
def diary():
	
	print("Sciccy : Tell me all about today")
	pyytsx3_jessica.say("Feel free to share")
	x = input(">>>")
	#date= input("Enter date in format (DD/MM/YYYY)\n")
	while (not(set(w.exit_words).intersection(x.split()))):
		
		if "add" in x.split() or "Add" in x.split():
			add_reminder_of_a_date()
			x = input(">>>")
		elif "read" in x.split() or "Read" in x.split():
			read_reminder()
			x = input(">>>")
		elif "delete" in x.split() or "Delete" in x.split():	
			delete_reminder()
			x = input(">>>")
		elif "thanku" in x.split() or "Thanku" in x.split() or "thanks" in x.split() or "Thanks" in x.split() or "thank you" in x or "Thank you" in x:	
			quit()
			x = input(">>>")
		else:
			pyytsx3_jessica.say("Entry do not match")
			x = input(">>>")



def valid_date(dates):	
	while True:
		
		dd , mm , yy = (int(x) for x in dates.split('-'))
		try:		
			s = datetime.date(yy,mm,dd)
			if s:
				return s	
			else:
				pyytsx3_jessica.say("Invalid date, enter again")
				dates = input("DD-MM-YYYY\n")

		except:
			pyytsx3_jessica.say("Invalid date, enter again")
			dates = input("DD-MM-YYYY\n")
			
		
#Function to add reminder in a file
def add_reminder_of_a_date():
	
	pyytsx3_jessica.say("Tell the date of format:")
	print("DD-MM-YYYY\n")
	dated = input()
	dateing = valid_date(dated)
	datein = str(dateing)
	#print(dateing)
	present = date.today()
	#print(present)
	#while datein < str(present):
	#	pyytsx3_jasper.say("Reminder cannot be set before today.Enter new date ")
	#	print("DD-MM-YYYY\n")
	#	dated = input()
	#	dateing = valid_date(dated)
	#	datein = str(dateing)	
	
	pyytsx3_jessica.say("Now tell the story")
	reminder_text = input(">>>")
	
	with open(reminder_path,"a") as f_reminder:
		f_reminder.write( str(datein) + "-" + str(reminder_text) + "\n")
	f_reminder.close()

	pyytsx3_jessica.say("your memory is safe here!")





#Function to read reminders	
def read_reminder():
	try:
		pyytsx3_jessica.say("Want to read datewise or read all?")
		i = input("Press \n read all. \n read according to date. \n quit\n")
		if "read all" in i or "Read all" in i or "all" in i.split() or "All" in i.split():	
			f = open(reminder_path,"r")
			for line in f:
				try:				
					print(line)
					pyytsx3_jessica.say(line)
				except:
					print("File empty")
				
			f.close()
		elif "read according to date" in i or "Read according to date" in i or "date" in i.split() or "Date" in i.split() or "datewise" in i.split() or "Datewise" in i.split():  
			pyytsx3_jessica.say("Enter the date of format:")
			print("DD-MM-YYYY")
			dated = input()
			datein = valid_date(dated)
			#print(datein)
			dateing = str(datein)	
			f = open(reminder_path,"r")
			flag = 0
			for line in f:
				try:	
					if dateing in line:
						print (line)
						pyytsx3_jessica.say(line)
						flag = 1
					else:
						flag = 0
				except:
					pyytsx3_jessica.say("Error in the program")
			if flag == 0:
				print("Nothing in the diary of this date")
				pyytsx3_jessica.say("Nothing in the diary of this date")	
			f.close()
		#elif "quit" in i.split() or "Quit" in i.split() or "Exit" in i.split() or "exit" in i.split():
		#	exit()

	except:
			pyytsx3_jessica.say("Wrong choice") 






#Function to edit reminders
def delete_reminder():


	try:
		pyytsx3_jessica.say("Want to remove  datewise or remove all?")
		i = input("Press \n remove all. \n remove according to date. \n quit\n")
		if "delete all" in i or "Delete all" in i or "all" in i.split() or "All" in i.split():
			try:
				f = open(reminder_path,'r+')
				for line in f:
					continue
				f.seek(0)
				f.truncate()
				f.close()
			except:
				pyytsx3_jessica.say("Cannot remove")

		elif "delete according to date" in i or "Delete according to date" in i or "date" in i.split() or "Date" in i.split() or "datewise" in i.split() or "Datewise" in i.split():

			f = open(reminder_path,"r+")
			data= []
			for line in f:
				print (line)
				data.append(line)
	
			pyytsx3_jessica.say("Tell the date you wqant to remove")
			print("DD/MM/YYYY")
			dated = input()
			datein = valid_date(dated)
			dateing = str(datein)	
			new_data= []
			for line in data:
				if dateing in line:
					if new_data in line:
						pyytsx3_jasper.say("No memory in the file")
					else:
						continue
					
				else:
					new_data.append(line)
			f.seek(0)
			f.writelines([line for line in new_data])
			f.truncate()
			f.close()
		#elif  "quit" in i.split() or "Quit" in i.split() or "Exit" in i.split() or "exit" in i.split():
		#	exit()



	except:
		pyytsx3_jessica.say("Wrong choice")


#diary()




