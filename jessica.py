import pyytsx3_jessica as pyt #own  (Edited)
import reboot #own 
import calendar_jessica as calen #own  (Edited)
import news_jessica as news
import wikipedia_jessica as wikiped  #own  (Edited)
import day_jessica as dayto #own  (Edited)
import wolfram_jessica as wolfram #own  (Edited)
import calculator_jessica as calcul #own  (Edited)
import quote_jessica as quo #own
import sendmail_jessica as mail #own
import config #own
import notes_jessica as note #own  
import alarm_jessica as alarms #own
import diary_jessica #own   (Edited)
import weather_jessica #own
import music_jessica as mus #own
import schedule_today as sch #own (Edited)
import reminder_jessica as remind #own  (Edited)
import jessica_words as w


from datetime import date
from datetime import datetime
from datetime import time
import time
import calendar
import sys
import random
import os

def wish_now():
	time1 = datetime.now()
	time_now = time1.strftime("%X")
	HH,MM,SS = (int(i) for i in time_now.split(':') )

	if HH >= 24 and HH < 12:	
		wi = "Good morning"
	elif HH >= 12 and HH <= 16:
		wi = "Good afternoon"
	elif HH >= 16 and HH <= 21:
		wi = "Good evening"
	else:
		wi = "Good night"

	return wi



wi = wish_now()
pyt.say( wi + config.Name + "   "  )
#print(str(wi) + " " + str(config.Name))
os.system('clear')
sch.schedule()
x = str(input(config.Name + ":"))




while True:
		
	#1.Wishing
	if list(set(x.split())&set(w.wishing_words)):
		messages = ["Hi", "Hey" ,"Hello","Hola"]
		message = random.choice(messages)	
		#pyt.say(message +" " + config.Name )
		pyt.say("What can i help you with?")
		x = str(input(config.Name + ":"))


	#Jessie's name
	elif list(set(x.split())&set(w.name_words)):
		pyt.say("My name is Jessica")
		x = str(input(config.Name + ":"))


	#2.what can you do?
	elif "What can you do" in x or "what can you do" in x:
		print("\n1.time and date \n2.Day of a date \n3.Calendar \n4.Reminders \n5.Diary \n6.Schedule managing \n7.Calculator \n8.News \n9.Weather \n10.Wolfram \n11.Notes \n12.Alarm \n13.Send mail \n14.Quotes \n15.Wikipedia \n")	
		pyt.say("time and date. Day of a date. Calendar. Reminders. Diary Schedule managing. Calculator. News. Weather. Wolfram. Notes. Alarm. Send mail. Quotes. Wikipedia.")
		x = str(input(config.Name + ":"))


	#3.help me
	elif list(set(x.split())&set(w.help_words)):
		pyt.say("If you are confused enter your options seperated by a comma.")
		a = input("\n>>>")
		b = a.split(',')
		choices = random.choice(b)
		pyt.say("You should:")
		print("\nYou should:" + str(choices))
		pyt.say(choices)
		pyt.say("Hope it helped .Want me to do anythin else?")
		x = str(input(config.Name + ":"))
	

	#4.what's up
	elif list(set(x.split())&set(w.whats_words)):
		messages = ["I am fine. Thank you.","I am good. How are you!","Just missed you","I am getting bore.Ask my something"]
		message = random.choice(messages)	
		pyt.say(message)
		x = str(input(config.Name + ":"))	

	#5.Reply of hows you
	elif "I am good" in x or "I am good thanks" in x or "i am good" in x or "i am good thanks" in x or "am Good" in x.split() or "Am good" in x.split():
		pyt.say("Okay, so what do you want me to do?")
		x = str(input(config.Name + ":"))
	
	#6.Fine reply
	elif "I am fine" in x or "i am fine" in x or "fine" in x.split() or "fine" in x.split():
		pyt.say("Cheer up boss. It will be a good day ahead. What do want me to help in?")
		x = str(input(config.Name + ":"))
	

	
	#7.Current time
	elif list(set(x.split())&set(w.time_words)):
		#calen.current_time()
		pyt.say("The time is:")
		time1 = datetime.now()
		pyt.say(time1.strftime("%X"))
		print(time1.strftime("%X"))
		x = str(input(config.Name + ":"))
	

	
	#8.Today's date
	elif list(set(x.split())&set(w.date_words)):
		calen.today_date()
		x = str(input(config.Name + ":"))


	
	#9.Tell the day of a date
	elif list(set(x.split())&set(w.day_words)):
		dayto.day_for_date()
		x = str(input(config.Name + ":"))

	#10.Calendar
	elif "Calendar" in x.split() or "calendar" in x.split():
		os.system('clear')
		calen.cal()
		x = str(input(config.Name + ":"))

		
	#11.Calculator
	elif list(set(x.split())&set(w.cal_words)):
		os.system('clear')
		calcul.calc()
		x = str(input(config.Name + ":"))
	

	#12.News
	elif list(set(x.split())&set(w.news_words)):
		os.system('clear')
		news.speak_news()
		x = str(input(config.Name + ":"))
	

	#13.Wolfram)
	elif "Wolfram" in x.split() or "wolfram" in x.split():
		os.system('clear')
		wolfram.wolf()
		x = str(input(config.Name + ":"))
	

	
	#14.Wikipedia
	elif list(set(x.split())&set(w.wiki_words)):
		wikiped.wiki()
		x = str(input(config.Name + ":"))
	

	
	#15.Qoutes
	elif list(set(x.split())&set(w.quo_words)):
		os.system('clear')
		quo.quotes_jessica(x)
		x = str(input(config.Name + ":"))
		

		
	#16.Notes
	elif list(set(x.split())&set(w.note_words)):
		os.system('clear')
		note.notes()
		x = str(input(config.Name + ":"))
	
	
	
	#17.Gmail or Email(Send mail complete + Read mail concatenation error(Not included))
	elif list(set(x.split())&set(w.gmail_words)):
		os.system('clear')
		pyt.say("Only send message updated")
		mail.send_mail()
		x = str(input(config.Name + ":"))
	

	
	#18.Choosing random(Error picking the first choice only.)
	#elif list(set(x.split())&set(ran_words)):
	#	works = [wikiped.wiki(),diary_jessie.diary(),wolfram.wolf,news.speak_news,quo.quotes_jessie]
	#	#work = work.split(',')
	#	choices = random.choice(works)
	#	choices()

		#, music , game, facebook/twitter,weather_jessie.wea()
	#	x = str(input(config.Name + ":"))
			
	
	
	#19.Today's Schedule(Completed)
	elif list(set(x.split())&set(w.sch_words)):
		os.system('clear')
		sch.schedule()
		x = str(input(config.Name + ":"))
	


	
	#20.My personal diary(Completed)
	elif list(set(x.split())&set(w.diary_words)):
		os.system('clear')
		diary_jessie.diary()
		x = str(input(config.Name + ":"))


	#21.My Music(Completed)
	elif "Music" in x.split() or "music" in x.split() or " My playlist" in x or "my playlist" in x:
		mus.music()	
		x = str(input(config.Name + ":"))

	
	
	#22.Alarams(Completed)
	elif "Alarm" in x.split() or "Set Alaram" in x or "alarm" in x.split() or "set alarm" in x:
		os.system('clear')
		alarms.alarm()
		x = str(input(config.Name + ":"))
		

	
	#23.Reminder module(Completed)
	elif list(set(x.split())&set(w.rem_words)):
		os.system('clear')
		remind.rem()
		x = str(input(config.Name + ":"))
	

	

	#23.Weather(Completed)
	elif list(set(x.split())&set(w.weather_words)):
		os.system('clear')
		weather_jessie.wea()
		x = str(input(config.Name + ":"))
	
	
	#24.Thanku statement(Completed)
	elif list(set(x.split())&set(w.thanks_words)):
		pyt.say("  Your Welcome " + config.Name)
		x = str(input(config.Name + ":"))	
	
	
	
	#25.End of Jessie(Completed)
	elif list(set(x.split())&set(w.exit_words)):
		messages = ["bye","tata","see you soon","come back soon","be safe","have a nice day"]
		message=random.choice(messages)
		pyt.say(message)
		exit()
		#reboot.handle()
	#If words did not matched
	else:
		pyt.say(" Not understood wanna try again? If no, say bye ")
		x = str(input(config.Name + ":"))


#END OF JESSIE
