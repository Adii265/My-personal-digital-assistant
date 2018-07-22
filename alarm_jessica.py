import datetime
from datetime import date
from datetime import time
from datetime import datetime
import time
import os
import subprocess

import pyytsx3_jessica as pyt
#import stt_jessica as st
import jessica_words as w



def alarm():
	sec_now = 0
	sec_then = 0
	pyt.say("   Enter the time of alarm of 24 Hour format:  ")
	#value = "00"
	#while(not(set(w.hour_words).intersection(value))):
	#	value = st.speak()
	#hh = value
	#while(not(set(w.min_words).intersection(value))):
	#	value = st.speak()
	#mm = value

	#tim = str(hh) + ":" + str(mm)
	tim = input("HH:MM\n")
	time_in_sec = check_time(tim)

	nowe = datetime.now()
	time_now = nowe.strftime("%X")
	HH,MM,SS = (int(i) for i in time_now.split(':') )
	sec_now = (HH * 3600) + (MM * 60) + SS
	



	if time_in_sec > 12 and sec_now > 12 and time_in_sec > sec_now:
		remaining_time = time_in_sec - sec_now
	elif time_in_sec > 12 and sec_now > 12 and time_in_sec < sec_now:
		remaining_time = (24*3600) - (time_in_sec - sec_now)		
	elif time_in_sec < 12 and sec_now > 12:
		remaining_time = sec_now - time_in_sec	
	elif time_in_sec > 12 and sec_now < 12:
		remaining_time = (24*3600) - time_in_sec + sec_now			
	elif time_in_sec < 12 and sec_now < 12 and time_in_sec < sec_now:
		remaining_time = (24*3600) - (sec_now - time_in_sec)			
	elif time_in_sec < 12 and sec_now < 12 and time_in_sec > sec_now:
		remaining_time = time_in_sec - sec_now 
	else:
		print("Wrong time")
	
	pyt.say("Alarm set for " + str(remaining_time) + " seconds.")		
	time.sleep(remaining_time)
	os.system("aplay /home/apoorva/Desktop/jasper/Jessie/alarm_music.wav")
	

def check_time(tim):
	hh,mm = (int(i) for i in tim.split(':'))
	if hh > 23:
		print("Wrong date format .Enter date again")
		tim = input("HH:MM:SS\n")
	if mm > 60:
		print("Wrong date format .Enter date again")
		tim = input("HH:MM:SS\n")
	else:
		sec_then = (hh *3600) + (mm * 60)
	return sec_then



#alarm()