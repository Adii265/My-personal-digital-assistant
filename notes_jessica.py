import config #own
import pyytsx3_jessica as pyt #own
import reboot #own
import jessica_words as w

import os
from datetime import date
import datetime
import calendar


def find_files():
	flag = 0
	for file in os.listdir("/home/apoorva/Desktop/Jessica"):
		if file.endswith(".txt"):
			flag = flag + 1
				
	return flag

def notes():
	os.system('clear')
	pyt.say(" Want to read add or delete notes?. To exit the program type exit.")
	print(" \nWant to read add or delete notes?. \nTo exit the program speak exit")
	x = input(">>>")
	while (not(set(w.exit_words).intersection(x.split()))):
	#To add reminder
		if "add" in x.split() or "add reminder" in x.split() or "Add" in x.split() or "Add reminder" in x:
			try:
				flag = find_files()
				if flag == 0:
					pyt.say("No file found, Enter the name of new file with extension.")
					file_name = input("File Name:")
				else:
					pyt.say("Files are:  ")
					for file in os.listdir("/home/apoorva/Desktop/Jessica"):
						if file.endswith(".txt"):
							print(file)
					pyt.say("Enter file name to open a file with extension")
					file_name = input("File Name:")
			except Exception as e:
				print(str(e))
		
			add_notes(file_name)
			x = input(">>>")
				
		#to read the reminder of the date
		elif "Read" in x.split() or "read" in x.split() or "read my reminder" in x or "Read my reminder" in x or "read reminder" in x or "Read reminder" in x or "Read reminders" in x or "read reminders" in x:
			#try:
			flag = find_files()
			if flag == 0:
				pyt.say("No file found")
			else:
				pyt.say("Files are:  ")
				for file in os.listdir("/home/apoorva/Desktop/Jessica"):
					if file.endswith(".txt"):
						print(file)
				pyt.say("Enter file name to read a file with extension")
				file_name = input("File Name:")

				

			#except Exception as e:
			#	print(str(e))
			if file_name in os.listdir("/home/apoorva/Desktop/Jessica"):
					read_notes(file_name)

			elif not(file_name in os.listdir("/home/apoorva/Desktop/Jessica")):
				while(not(file_name in os.listdir("/home/apoorva/Desktop/Jessica"))):
					pyt.say("File not found.Enter again.")
					file_name = input("File Name:")
				if file_name in os.listdir("/home/apoorva/Desktop/Jessica"):
					read_notes(file_name)
			x = input(">>>")

			
		#To edit the reminder
		elif "Edit" in x.split() or "edit" in x.split() or "Delete" in x.split() or "delete" in x.split() or "delete reminder" in x or "Delete reminder" in x or "edit reminder" in x.split() or "Edit reminder" in x.split():
			try:
				flag = find_files()
				if flag == 0:
					pyt.say("No file to delete")
				else:
					pyt.say("Files are:  ")
					for file in os.listdir("/home/apoorva/Desktop/Jessica"):
						if file.endswith(".txt"):
							print(file)
					pyt.say("Which file to delete?")
					file_name = input("File Name:")
			except Exception as e:
				print(str(e))
			delete_notes(file_name)
			x = input(">>>")
		
		#To end the calendar module
		elif "thanks" in x.split() or "thanku" in x.split() or "Thanks" in x.split() or "Thanku" in x.split():
			pyt.say("Your welcome")

		#if words do not match
		else:
			pyt.say("Not understood! Please say again.")
			x = input(">>>")
		


	



def add_notes(file_name):
	pyt.say("Do you want to add notes for today?")
	ans = input(config.Name + ": ")
	if ans == "Yes" or ans == "yes" or ans =='y' or ans == "Y":
		todays = date.today()		
		dates = str(todays)
	else:
		pyt.say("Enter the date of format:\n")
		dateing = input("DD/MM/YYYY\n")
		dateing = valid_date(dateing)
		dates = str(dateing)
		
	#Searching for the date in file
	
	pyt.say("Start adding notes")
	notes_text = input()
	with open(file_name,"a") as f_notes:
		f_notes.write(str(dates) + " - " + notes_text + "\n")
	
	f_notes.close()
	pyt.say("Notes noted")




def read_notes(file_name):
	
	pyt.say("Want to read the whole file or read a particular date")
	i = input(">>>")
	if "read all" in i or "Read all" in i or "all" in i.split() or "All" in i.split():
		f = open(file_name,"r")
		for line in f:
			try:				
				print(line)
				pyt.say(line)
			except:
				pyt.say("File empty")
	
	elif "read according to date" in i or "Read according to date" in i or "date" in i.split() or "Date" in i.split() or "datewise" in i.split() or "Datewise" in i.split():
		pyt.say("Enter the date of format:\n")
		dated = input("DD/MM/YYYY\n")		
		datein = valid_date(dated)
		dates = str(datein)
		f = open(file_name,"r")
		flag = 0
		for line in f:
			try:	
				if dateing in line:
					print (line)
					pyytsx3_jasper.say(line)
					flag = 1
				else:
					flag = 0
			except:
				pyytsx3_jasper.say("Error in the program")
		if flag == 0:
			print("Nothing on the calendar on this date")	
		f.close()



def delete_notes(file_name):
	try:
		pyt.say("Want to remove  datewise or remove all?")
		i = input("Want to remove a file or remove according to date")
		if "delete all" in i or "Delete all" in i or "all" in i.split() or "All" in i.split():
			try:
				f = open(file_name,'r+')
				for line in f:
					continue
				f.seek(0)
				f.truncate()
				f.close()
				files = "/home/apoorva/Desktop/jasper/Jessie/" + str(file_name)
				print(files)
				if os.path.isflie(files):
					pyt.say("Removing file"+str(files))
					os.remove(files)
				else:
					pyt.say("File not found")
			except:
				pyt.say("Cannot remove")

		elif "delete according to date" in i or "Delete according to date" in i or "date" in i.split() or "Date" in i.split() or "datewise" in i.split() or "Datewise" in i.split():

			f = open(file_name,"r+")
			data= []
			#for line in f:
			#	print (line)
			#	data.append(line)
	
			pyt.say("Tell the date of the reminder of format:")
			print("DD/MM/YYYY")
			dated = input()
			if dated == "today":
				todays = dated.today()
				dates = str(todays)	

			else:
				datein = valid_date(dated)
				dates = str(datein)

			new_data= []
			for line in data:
				try:
					if dates in line:
						continue
				
					else:
						new_data.append(line)
				except:
					print("Date not found")
			f.seek(0)
			f.writelines([line for line in new_data])
			f.truncate()
			f.close()
	

	except:
		pyt.say("Wrong choice")




#Function to check a valid date	
def valid_date(dates):	
	while True:
		
		dd , mm , yy = (int(x) for x in dates.split('-'))
		try:		
			s = datetime.date(yy,mm,dd)
			if s:
				return s	
			else:
				pyytsx3_jasper.say("Invalid date, enter again")
				dates = input("DD-MM-YYYY\n")

		except:
			pyytsx3_jasper.say("Invalid date, enter again")
			dates = input("DD-MM-YYYY\n")
			


#notes()