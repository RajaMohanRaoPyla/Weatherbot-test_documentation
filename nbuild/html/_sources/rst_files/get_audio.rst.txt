Record the voice from the user
===================================

Here record the voice signal using the microphone. The city name as to be given.Here is the program for detecting the voice signal for the user. 


.. code-block:: python
   
   # get audio from the microphone                                                                       
   r = sr.Recognizer()                                                                                   
   with sr.Microphone() as source:                                                                       
       print("Speak:")                                                                                   
       audio = r.listen(source)  
