from gtts import gTTS 
import os
import time

def tts_msg(msg, language) :   
    speech = gTTS(text = msg, lang = language, slow = False)
    speech.save("text.mp3")
    os.system("start text.mp3")

start_time = time.time()
tts_msg("horseleft1meter", 'en')
print("--- %s seconds ---" % (time.time() - start_time))
