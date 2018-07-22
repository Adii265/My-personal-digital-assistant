import reboot
import pyytsx3_jessica as pyt
import config



from weather import Weather, Unit
#import pyowm

#api_key = pyowm.OWM(API_key = "563b68e3b0784bbeb5f112116180307", subscription_type = "Premium")

#def wea():

#	observation = api_key.weather_at_place("MUMBAI,India")
#	w = observation.get_weather()
#	temperature_C = w.get_temperature('celsius')
#	temperature_F = w.get_temperature('farhenheit')
#	tommorow = pyowm.timeutils.tommorrow()
#	wind = w.get_wind()


#	print(w)
#	print(wind)
#	print(temperature_C)
#	print(temperature_F)
#	print(tommorrow)


def wea():
	weather = Weather(unit = Unit.CELSIUS)
	location = weather.lookup_by_location("Allahabad")
	
	#To find the todays weather:
	condition = location.condition
	pyt.say("\nTodays weather is: " +  str(condition.text))
	print("\nTodays weather is: " +  str(condition.text))

	
	pyt.say("Want to find future weather?")
	ans = input(">>>")

	#To find weather forcast for next 10 days:
	if ans == 'Y' or ans == "y" or ans == "Yes" or ans == "yes":
		forecasts = location.forecast
		for forecast in forecasts:
		    
			print("\n Date:" + str(forecast.date))
			pyt.say(" On date " + str(forecast.date))
			print("Expected :" + str(forecast.text))
			pyt.say("The weather is expected to be :" + str(forecast.text))
			#print("Highest temperature:" + str(forecast.high))
			#print("Lowest temperature:" + str(forecast.low))
	

	else:
		pyt.say("Okay bye")
		

	








