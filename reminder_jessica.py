import pyytsx3_jessica as pyt
import jessica_words as w


from datetime import datetime
from datetime import date
from datetime import time
from datetime import datetime
import time
import calendar
import sys
import datetime
import os


reminder_path = "reminder_jessica.txt"
def rem():
	os.system('clear')
	print("\nWant to add, read or delete or edit reminder?")
	pyt.say("Want to add, read or delete or edit reminder?")
	x = input(">>>")
	while (not(set(w.exit_words).intersection(x.split()))):
	#date= input("Enter date in format (DD-MM-YYYY)\n")
	
		#To add reminder
		if "add" in x.split() or "add reminder" in x.split()or "Add reminder" in x or "Add" in x.split():
			add_reminder_of_a_date()
			x = input(">>>")
	
		#to read the reminder of the date
		elif "Read" in x.split() or "read" in x.split() or "read my reminder" in x or "Read my reminder" in x or "read reminder" in x or "Read reminder" in x or "Read reminders" in x or "read reminders" in x:
			read_reminder()
			x = input(">>>")

		#To edit the reminder
		elif "Edit" in x.split() or "edit" in x.split() or "Delete" in x.split() or "delete" in x.split() or "delete reminder" in x or "Delete reminder" in x or "edit reminder" in x.split() or "Edit reminder" in x.split():
			delete_reminder()
			x = input(">>>")
			

		#if words do not match
		else:
			pyt.say("Not understood! Please say again.")
			x = input(">>>")
	
	#except Exception as e:
	#	print(str(e))





#Function to check a valid date	
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
			
		
#Function to add reminder in a file
def add_reminder_of_a_date():
	
	pyt.say("Tell the date of the reminder of format:")
	print("DD-MM-YYYY\n")
	dated = input()
	dateing = valid_date(dated)
	datein = str(dateing)
	#print(dateing)
	present = date.today()
	#print(present)
	while datein < str(present):
		pyt.say("Reminder cannot be set before today.Enter new date ")
		print("DD-MM-YYYY\n")
		dated = input()
		dateing = valid_date(dated)
		datein = str(dateing)	
	
	pyt.say("Now set the reminder")
	reminder_text = input(">>>")
	
	with open(reminder_path,"a") as f_reminder:
		f_reminder.write( str(datein) + "-" + str(reminder_text) + "\n")
	f_reminder.close()

	pyt.say("reminder succesfully set.")





#Function to read reminders	
def read_reminder():
	#try:
	pyt.say("Want to read datewise or read all?")
	i = input("Press \n read all. \n read according to date. \n quit\n")
	if "read all" in i or "Read all" in i or "all" in i.split() or "All" in i.split():	
		f = open(reminder_path,"r")
		for line in f:
			try:				
				print(line)
				pyt.say(line)
			except:
				print("File empty")
			
		f.close()
	elif "read according to date" in i or "Read according to date" in i or "date" in i.split() or "Date" in i.split() or "datewise" in i.split() or "Datewise" in i.split():  
		pyt.say("Enter the date of format:")
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
					pyt.say(line)
					flag = 1
				else:
					flag = 0
			except:
				pyt.say("Error in the program")
		if flag == 0:
			print("Nothing on the calendar on this date")	
		f.close()
	elif "quit" in i.split() or "Quit" in i.split() or "Exit" in i.split() or "exit" in i.split():
		exit()

	#except:
	#		pyt.say("Wrong choice") 






#Function to edit reminders
def delete_reminder():


	try:
		pyt.say("Want to remove  datewise or remove all?")
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
				pyt.say("Cannot remove")

		elif "delete according to date" in i or "Delete according to date" in i or "date" in i.split() or "Date" in i.split() or "datewise" in i.split() or "Datewise" in i.split():

			f = open(reminder_path,"r+")
			data= []
			for line in f:
				print (line)
				data.append(line)
	
			pyt.say("Tell the date of the reminder of format:")
			print("DD/MM/YYYY")
			dated = input()
			datein = valid_date(dated)
			dateing = str(datein)	
			new_data= []
			for line in data:
				if dateing in line:
					if new_data in line:
						pyt.say("No reminder in file")
					else:
						continue
					
				else:
					new_data.append(line)
			f.seek(0)
			f.writelines([line for line in new_data])
			f.truncate()
			f.close()
		elif  "quit" in i.split() or "Quit" in i.split() or "Exit" in i.split() or "exit" in i.split():
			exit()



	except:
		pyt.say("Wrong choice")






#rem()

#add_reminder_of_a_date()
#read_reminder()
#delete_reminder()
