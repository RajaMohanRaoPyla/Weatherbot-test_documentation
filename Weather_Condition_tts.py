import requests
import speech_recognition as sr  
import datetime
# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

def Audio_to_text(audio):
	try:
	    print("You said " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("Could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results; {0}".format(e))

	city_name = str(r.recognize_google(audio).split(' ')[-1])
    return(city_name)

def get_woeid(city_name):
	r = requests.get('https://www.metaweather.com/api/location/search/?query='+ str(city_name))
	woeid = r.json()[0]['woeid']
	return(get_weather_stats(woeid))


def get_weather_stats(woeid):
	date = datetime.datetime.now().strftime("%Y/%m/%d")
	r = requests.get('https://www.metaweather.com/api/location/'+str(woeid)+"/"+date)
	weather_state = r.json()[0]['weather_state_name']
	temperature = r.json()[0]['the_temp']
	return(weather_state,temperature)

city_name = Audio_to_text(audio)
weather_type, temp = get_woeid(city_name)


from gtts import gTTS
from io import BytesIO
from playsound import playsound


my_variable = "the weather in {} is {} with a temperature of {} degrees".format(city_name,weather_type,temp)
# import pyttsx3

# engine = pyttsx3.init()
# engine.say(my_variable)
def tts_audio_saver(my_variable):
	tts = gTTS(my_variable, 'en')
	tts.save("MusicFile.mp3")
	return playsound('MusicFile.mp3')


tts_audio_saver(my_variable)
# sudo apt-get install python3-pyaudio
