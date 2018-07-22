import os


import pyytsx3_jessica as pyt





def music():
	for file in os.listdir("/home/apoorva/Desktop/Jessica/music"):
		if file.endswith(".wav") or file.endswith(".mp3"):
			print("\n" + file)
	pyt.say("To stop the music press Ctrl+C ...These are the files in the folder. Which file you want to play?")
	file_name = input("\nFile name:\n")
	flag = 0		
	for file in os.listdir("/home/apoorva/Desktop/Jessica/music"):
		if file_name in file:
			flag = 1	
	if flag == 0:
		pyt.say("File name not exists.")		
	else:
		os.system("aplay /home/apoorva/Desktop/Jessica/music/"+file_name)


