
Program for Text to Audio
=================================


.. code-block:: python

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

