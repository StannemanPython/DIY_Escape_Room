import time
from datetime import timedelta, datetime
from threading import *

#countdown is the start of the timer so that I can let the guests of
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
  for i in range(4):
    t = 6*60
    while t:
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line
      time.sleep(1)
      t -= 1
    print("You took too much time! You lose!")
    time.sleep(60)

#pomodora is the PIN input with the different WIN and LOSE returns
def pomodoro():

    print("The Escape Room starts now. Find the 4 digits of the pincode. Write the digits in order from lowest to highest. You only have 3 tries")
    timer_start = datetime.now()
    secret_code = "3389"
    allotted_time = timedelta(seconds=6*60)
    error = 0
    while True:
        print("Enter the 4 digit pincode here:")
        code = input()
        now = datetime.now()
        time_taken = now - timer_start
        if time_taken > allotted_time:
            print("You took too much time! You lose!")
            time.sleep(60)
            return
        if code == secret_code:
            print("You managed to stop the mutation and escaped! You won!")
            time.sleep(60)
            return
        print("That's not the right code!")
        error += 1
        if error == 3:
            print("You took too many tries! You lose!")
            time.sleep(60)
            return
        print(f"You only have {allotted_time - time_taken} time left!")

t1 = Thread(target=soup)
t2 = Thread(target=pomodoro)
t1.start() #Calls first function
t2.start() #Calls second function to run at same time

