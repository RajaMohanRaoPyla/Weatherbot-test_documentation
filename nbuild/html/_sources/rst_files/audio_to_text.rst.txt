
Convert the Audio to Text
==============================

Speech Recognition is an important feature in several applications used such as home automation, artificial intelligence, etc. This article aims to provide an introduction on how to make use of the SpeechRecognition library of Python. This is useful as it can be used on microcontrollers such as Raspberri Pis with the help of an external microphone.


.. code-block:: python
   

   def Audio_to_text(audio):
       try:
           print("You said " + r.recognize_google(audio))
       except sr.UnknownValueError:
           print("Could not understand audio")
       except sr.RequestError as e:
           print("Could not request results; {0}".format(e))

       city_name = str(r.recognize_google(audio).split(' ')[-1])
   return(city_name)




