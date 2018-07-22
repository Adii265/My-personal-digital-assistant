import sys
import os
import re
import random
import subprocess


import pyytsx3_jessica as pyt #own


def handle():
	
	messages=["Bye-Bye","TA-TA","I am going to sleep","See you soon","Have a nice day"]
	message=random.choice(messages)
	pyt.say(message)
	
	command = "/usr/bin/sudo /sbin/shutdown -r now"
	import subprocess
	process = subprocess.Popen(command.split(), stdout = subprocess.PIPE)
	output = process.communicate()[0]



