import threading
from threading import Thread
from threading import Timer
import time

class BackgroundTimer(Thread):   
   def run(self):
      while 1:
        time.sleep(1)
        # do something
        print('a')


# ... SNIP ...
# Inside your main thread
# ... SNIP ...

timer = BackgroundTimer()
timer.start()
print('Started Timer')
#input('Hit Enter to kill the thread.')
print('Literally Doing Nothing!')
input()
time.sleep(50)
