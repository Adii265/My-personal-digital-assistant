import wikiquote
import pyytsx3_jessica as pyt
import random



def quotes_jessica(a):
	if str(a) == "Inspire" or str(a) == "inspire":
		y = ['life','happiness','success','love','family','dedication','work','hard work','friends','lucky']
		z = random.choice(y)
		print( wikiquote.quotes(z,max_quotes = 1) )
		pyt.say( wikiquote.quotes(z,max_quotes = 1) )

	elif str(a) == "quotes" or str(a) == "Quotes":
		pyt.say("Search quote about:")
		y = input(">>>")
		print( wikiquote.quotes(y,max_quotes = 1) )
		pyt.say( wikiquote.quotes(y,max_quotes = 1) )
	
	
	elif str(a) == "Quote" or str(a) == "quote" :	
		print( wikiquote.quote_of_the_day())
		pyt.say( wikiquote.quote_of_the_day() )

	#elif str(a) == "Random" or str(a) == "random":
	#	y = ['life','happiness','success','love','family','dedication','work','hard work','friends','lucky']
	#	z = random.choice(y)
	#	print( wikiquote.quotes(z,max_quotes = 1) )
	#	pyt.say( wikiquote.quotes(z,max_quotes = 1) )
	else:
		
		pyt.say("Quotes not found")

