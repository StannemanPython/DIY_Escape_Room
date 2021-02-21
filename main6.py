import time
import threading
from tkinter import *
window = Tk()
window.title("Escape Room")
window.geometry("500x400")

#soup is the countdown timer that has to run
def soup():
  for i in range(4):
    t = 90*60
    while t:
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      my_label4.config(text=timer)
      time.sleep(1)
      t -= 1
    my_label3.config(text="You took too much time! You lose!", fg="red", font=("Times", "24", "bold"))
    time.sleep(60)

def only_numbers(char):
    return char.isdigit()

error = 0
#pomodora is the PIN input with the different WIN and LOSE returns
def tomato():
    num = (my_entry.get())
    secret_code = "3389"
    global error  # inform funtion to use external variable `count`
    error = error + 1
    if num != secret_code:
        my_label3.config(text="That's not the right code!")
    if num == secret_code:
        my_label3.config(text="Congratulations! You managed to stop the mutation and escaped! You won!", fg="green", font=("Times", "24", "bold"))
        #I need to stop the time here
    if error == 3:
        my_label3.config(text="You took too many tries! You lose!", fg="red", font=("Times", "24", "bold"))

my_label1 = Label(window, text = "The Escape Room starts now. Find the 4 digits of the pincode. You only have 3 tries")
my_label1.grid(row=0, column=0)

my_label2 = Label(window, text = "Enter PIN")
my_label2.grid(row=3, column=0) #this is placed at 0, 0

my_label3 = Label(window, text = "")
my_label3.grid(row=4, column=0)

my_label4 = Label(window, text="")
my_label4.grid(row=0, column=1)

validation = window.register(only_numbers)
my_entry = Entry(window, validate="key", validatecommand=(validation, '%S'))
my_entry.grid(row=3, column=1)

my_button = Button(window, text="Check PIN code", command=tomato)
my_button.grid(row=3, column=2)

threading.Thread(target=soup).start()

window.mainloop()


