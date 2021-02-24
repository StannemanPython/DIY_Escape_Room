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
      my_label4.config(text=timer, font=("Calibri", "60", "bold"))
      time.sleep(1)
      t -= 1
    my_label3b.config(text="You took too much time! You lose!", fg="red", font=("Calibri", "24", "bold"))
    my_button.destroy()
    my_entry.destroy()
    my_label2.destroy()
    my_label3.destroy()
    my_label4.destroy()
    time.sleep(60)

def only_numbers(char):
    return char.isdigit()

error = 0
#pomodora is the PIN input with the different WIN and LOSE returns
def tomato():
    num = (my_entry.get())
    secret_code = "3389"
    global error  # inform function to use external variable `count`
    error = error + 1
    if num != secret_code:
        my_label3b.config(text="That's not the right PIN!", font=("Calibri", "11"))
    if num == secret_code:
        my_label3.config(text="Congratulations! You managed to stop the mutation and escaped! You won!", fg="green", font=("Calibri", "24", "bold"))
        my_button.destroy()
        my_entry.destroy()
        my_label2.destroy()
        my_label3b.destroy()
        threading.Thread(target=soup).stop()
    if error == 3:
        my_label3b.config(text="You took too many tries! You lose!", fg="red", font=("Calibri", "24", "bold"))
        my_button.destroy()
        my_entry.destroy()
        my_label2.destroy()
        my_label3.destroy()
        my_label4.destroy()

my_label1 = Label(window, text = "The Escape Room has started. Find the 4 digit combination of the PIN. You only have 3 tries", font=("Calibri", "18"))
my_label1.place(x=100, y=0)

my_label2 = Label(window, text = "Enter PIN:", font=("Calibri", "10"))
my_label2.place(x=450, y=100)

my_label3 = Label(window, text="")
my_label3.place(x=100, y=300)

my_label3b = Label(window, text="")
my_label3b.place(x=100, y=300)

my_label4 = Label(window, text="")
my_label4.place(x=500, y=150)

validation = window.register(only_numbers)
my_entry = Entry(window, validate="key", validatecommand=(validation, '%S'))
my_entry.place(x=520, y=100)

my_button = Button(window, text="Check PIN", font=("Calibri", "10"), command=tomato)
my_button.place(x=650, y=95)

threading.Thread(target=soup).start()

window.mainloop()


