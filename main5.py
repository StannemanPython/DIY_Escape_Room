import time
from datetime import timedelta, datetime
from threading import *
import subprocess, sys
import threading

# the escape room know that the escape room is about to start.

global_game_time = 6*60 
#soup is the countdown timer that has to run
def soup():
    global global_game_time
    local_game_copy = global_game_time
    while local_game_copy:
        mins = local_game_copy // 60
        secs = local_game_copy % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\033[A" + timer)
        #print(timer,end="\r")
        time.sleep(1)
        local_game_copy -= 1
        global_game_time -= 1
        if local_game_copy == 0:
            break
    print("You took too much time! You lose!")
    time.sleep(60)
    

#pomodora is the PIN input with the different WIN and LOSE returns
def pomodoro():
    print("The Escape Room starts now. Find the 4 digits of the pincode. Write the digits in order from lowest to highest. You only have 3 tries")
    secret_code = "3389"
    error = 0
    with Lock(): 
        while error != 3:
            print("\n Enter the pin here: ")
            code = input("\n")
            if code == secret_code:
                print("You managed to stop the mutation and escaped! You won!")
                time.sleep(60)
                threading.Release()
                return True
            else:
                print("That's not the right code!")
                error += 1
    print("You took too many tries! You lose!")
    time.sleep(60)
    return False

t1 = Thread(target=soup)
t2 = Thread(target=pomodoro)
t1.start() #Calls first function
t2.start()

