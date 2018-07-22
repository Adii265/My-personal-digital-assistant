#import speech_recognition as sr




import pyytsx3_jessica as pyt


import speech_recognition as sr


#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))




r = sr.Recognizer()
m = sr.Microphone(device_index=0)

def speak():
	try:
		#print("A moment of silence, please...")
		with m as source: 
			r.adjust_for_ambient_noise(source)
		print("Set minimum energy threshold to {}".format(r.energy_threshold))
		while True:
			#pyt.say("Say something!")
			#print("Say something!")
			with m as source:
				audio = r.listen(source)
			print("Got it!")
			pyt.say("Got it!")
			try:
				# recognize speech using Google Speech Recognition
				value = r.recognize_google(audio)
				# we need some special handling here to correctly print unicode characters to standard output
				if str is bytes:  
					# this version of Python uses bytes for strings (Python 2)
					print("You said {}".format(value).encode("utf-8"))
					pyt.say("You said {}".format(value).encode("utf-8"))
				else:  
					# this version of Python uses unicode for strings (Python 3+)
					print("You said {}".format(value))
					pyt.say("You said {}".format(value))
			except sr.UnknownValueError:
				print("Oops! Didn't catch that")
				pyt.say("Oops! Didn't catch that")
			except sr.RequestError as e:
				print("Uh oh! Internet problem")
				pyt.say("Uh oh! Internet problem")
	except KeyboardInterrupt:
		pass

	return value
#speak()
