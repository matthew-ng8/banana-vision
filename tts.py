import multiprocessing,threading, queue
from multiprocessing import Queue
import pyttsx3

# class tts_engine:
#     def __init__(self) -> None:
#         self.engine = pyttsx3.init()
#         if(self.engine == None):
#             print("enginer is None type ")
#         self.engine.say("Starting up")
#         self.engine.runAndWait()
    
#     def msg(self, message = "Welcome to Banana Vision",rate = 280, volume = 100.0):
#         self.engine.setProperty('rate', rate)     # setting up new voice rate
#         self.engine.setProperty('volume', volume)    # setting up volume level between 0 and 1
#         voices = self.engine.getProperty('voices')       #getting details of current voice
#         self.engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
#         self.engine.say(message)


#     def tts_process(q, tts_engine):
#         while(True):
#             msg = str(q.get())
#             print("in thread" + msg + "\n")
#             tts_engine.msg(msg)

class TTSProcess(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        self.daemon = False
        self.start()
    def run(self):
        tts_engine = pyttsx3.init()
        tts_engine.setProperty('rate', 280)     # setting up new voice rate
        tts_engine.setProperty('volume', 100.0)    # setting up volume level between 0 and 1
        tts_engine.startLoop(False)
        t_running = True
        while t_running:
            if self.queue.empty():
                tts_engine.iterate()
            else:
                data = self.queue.get()
                if data == "exit":
                    t_running = False
                else:
                    tts_engine.say(data)
        tts_engine.endLoop()


# class TTSThread(threading.Thread):
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         self.queue = queue
#         self.daemon = True
#         self.start()

#     def run(self):
#         tts_engine = pyttsx3.init()
#         tts_engine.setProperty('rate', 280)     # setting up new voice rate
#         tts_engine.setProperty('volume', 100.0)    # setting up volume level between 0 and 1
#         tts_engine.startLoop(False)
#         t_running = True
#         while t_running:
#             if self.queue.empty():
#                 tts_engine.iterate()
#             else:
#                 data = self.queue.get()
#                 if data == "exit":
#                     t_running = False
#                 else:
#                     tts_engine.say(data)
#         tts_engine.endLoop()

if __name__ == "__main__":
    # start_time = time.time()
    # tts_msg("ayo watch out theres a wall", 180, 1.0)
    # print("--- %s seconds ---" % (time.time() - start_time))
    q = queue.Queue()
    tts_thread = TTSThread(q)
    for item in range(30):
        print("main : " + str(item) + "\n")
        q.put(item)
    q.join()
    print('All work completed')

