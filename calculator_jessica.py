import pyytsx3_jessica #own
import reboot #own
import jessica_words as w



def divide(a,b):
	float(a),float(b)
	if a==0:
		return 0
	elif b==0:
		pyt.say("division impossible")
	else:
		return float(a/b)


def calc():

	pyytsx3_jessica.say("This module can simply add or subtract or multiply or divide two numbers")
	z = input(">>>")
	while (not(set(w.exit_words).intersection(z.split()))):
		
		#To add
		if "add" in z.split() or "Add" in z.split():
			s = 0
			x = int(input("the first number"))
			y = int(input("the second number") )
			s = x+y
			print(s)
			pyytsx3_jessica.say(s)
			z = input(">>>")
	
		#to subtract
		if "subtract" in z.split() or "Subtract" in z.split():
			x = int(input("the first number"))
			y = int(input("the second number") )	
			diff = x-y
			print(diff)
			pyytsx3_jessica.say(diff)
			z = input(">>>")

		#To multiply
		if "multiply" in z.split() or "Multiply" in z.split():
			x = int(input("the first number"))
			y = int(input("the second number")) 			
			mul =x*y
			print(mul)
			pyytsx3_jessica.say(mul)
			z = input(">>>")
	
		#To divide
		if "divide" in z.split() or "Divide" in z.split():
			x = float(input("the first number"))
			y = float(input("the second number")) 
			div = divide(x,y)
			print(div)
			pyytsx3_jessica.say(div)
			z = input(">>>")
		
	
		#Other words
		else:
			pyytsx3_jessica.say("Words didnot matched. please say again!")
			z = input(">>>")
	
	

#calc()