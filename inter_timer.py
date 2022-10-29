import time
import random
from playsound import playsound 

min_time = int(input("Minimum time in mins:"))
max_time = int(input("Max time in mins:"))
    
def i_timer():
    timer = random.randint(min_time, max_time)
    t = timer*60
    while t:
        time.sleep(1)
        t -= 1
    playsound("sci_fi_alarm.mp3")
    i_timer()

i_timer()
