import pyttsx3
import time

def tts_msg(msg, rate, volume) : 
    engine = pyttsx3.init() # object creation 
    engine.setProperty('rate', rate)     # setting up new voice rate
    engine.setProperty('volume', volume)    # setting up volume level between 0 and 1
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say(msg)
    engine.runAndWait()
    engine.stop()
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
    

start_time = time.time()
tts_msg("ayo watch out theres a wall", 180, 1.0)
print("--- %s seconds ---" % (time.time() - start_time))