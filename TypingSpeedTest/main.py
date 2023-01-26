from tkinter import *
from texts import texts_dic
import random

index = random.randint(1,5)
quiz_text = texts_dic[index]

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=700, height=500)

canvas = Canvas(width=100, height=50, bg="#876445")
timer_text = canvas.create_text(53, 30, text="0", fill="white", font=("Arial", 20, "bold"))
canvas.pack()

mission = Label(text="Type the sentence below as fast as you can!", font=("Arial", 24, "bold"))
mission.pack()

sentence = Label(text=quiz_text, font=("Arial", 18))
sentence.pack()

typing_field = Entry(width=70)
typing_field.pack()

count=0
def timer_start(count):
    canvas.itemconfig(timer_text, text=count)
    global updated_time
    updated_time = canvas.after(1000, timer_start, count + 1)

def timer_off():
    canvas.after_cancel(updated_time)

def start_clicked():
    mission.config(text=f"Start typing.")
    start.destroy()
    timer_start(count)

def check_entry():
    time = updated_time.split("#")[1]
    stop.destroy()
    timer_off()
    entry_text = typing_field.get()
    mission.config(text="Stop typing.")
    if entry_text == quiz_text:
        result =Label(text=f"\nYou typed correctly. Your typing speed was: {time} seconds", font=("Arial", 18, "bold"))
        result.pack()
    else:
        print(entry_text == quiz_text)
        print(entry_text)
        print(quiz_text)
        result = Label(text="\nYou typed wrong. Try again.", font=("Arial", 18, "bold"))
        result.pack()

start = Button(text="Start", command=start_clicked)
start.pack()

stop = Button(text="Stop", command=check_entry)
stop.pack()

# Has to be at the end of code
window.mainloop()
