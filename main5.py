import time
from datetime import timedelta, datetime
from threading import *
import subprocess, sys
import curses

#countdown is tihe start of the timer so that I can let the guests of
# the escape room know that the escape room is about to start.

def countdown(t):
    while t:  # while t > 0 for clarity
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # overwrite previous line
        time.sleep(1)
        t -= 1
    print('Blast Off!!!')


t = input("Enter the time in seconds: ")

countdown(int(t))


#soup is the countdown timer that has to run
def soup():
    screen = curses.initscr()
    t = 6 * 60
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #print(timer, end="\r", flush=True) # overwrite previous line
        screen.addstr(0,0,timer)
        time.sleep(1)
        screen.refresh()
        t -= 1
        if t == 0:
            break
    print("You took too much time! You lose!")
    time.sleep(60)
    

#pomodora is the PIN input with the different WIN and LOSE returns
def pomodoro():
    input_screen = curses.initscr()
    print("The Escape Room starts now. Find the 4 digits of the pincode. Write the digits in order from lowest to highest. You only have 3 tries")
    secret_code = "3389"
    error = 0
    #code = input("Enter the PIN here: \n")
    while error != 3:
        code = input("enter the PIN here: ")
        if code == secret_code:
            print("You managed to stop the mutation and escaped! You won!")
            time.sleep(60)
            exit()
        else:
            print("That's not the right code!")
            error += 1
        
    print("You took too many tries! You lose!")
    time.sleep(60)
    return False
    #print(f"You only have {allotted_time - time_taken} time left!")

t1 = Thread(target=soup)
t2 = Thread(target=pomodoro)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time

    
