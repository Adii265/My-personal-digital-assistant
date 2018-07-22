import smtplib

import config #own
import pyytsx3_jessica as pyt #own


def send_mail():

	
	
	pyt.say("who will be the reciever?")
	name = input()
	try:
		if "Aditi" in name or "aditi" in name:
			to = config.Aditi
		if "Rachita" in name or "rachita" in name:
			to = config.Rachita
		if "Jasper" in name or "jasper" in name:
			to = config.EMAIL_ADDRESS
		if "Apoorva" in name or "apoorva" in name:
			to = config.Apoorva
	except :
		
 		to = str(input("Enter email address"))

	#pyt.say("Speak the message")
	pyt.say("Enter the message")
	msg = input()
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	froma = config.EMAIL_ADDRESS
	psw = config.PASSWORD
	server.login( froma , psw )  
	server.sendmail( froma , to , msg )
	print('Message Sent..')
	server.quit()



