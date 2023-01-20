from tkinter import *
window = Tk()
window.title("Typing Speed Test")
window.minsize(width=700, height=500)
# window.config(bg="#76BA99")

canvas = Canvas(width=100, height=50, bg="#876445")
timer_text = canvas.create_text(53, 30, text="0", fill="white", font=("Arial", 20, "bold"))
canvas.pack()

mission = Label(text="Type the sentence below as fast as you can!", font=("Arial", 24, "bold"))
mission.pack()

sentence = Label(text="\nSusie works in a shoeshine shop.\n Where she shines she sits, and where she sits she shines.\n", font=("Arial", 18))
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
    if entry_text == "Susie works in a shoeshine shop. Where she shines she sits, and where she sits she shines.":
        result =Label(text=f"\nYou typed correctly. Your typing speed was: {time} seconds", font=("Arial", 18, "bold"))
        result.pack()
    else:
        result = Label(text="\nYou typed wrong. Try again.", font=("Arial", 18, "bold"))
        result.pack()

start = Button(text="Start", command=start_clicked)
start.pack()

stop = Button(text="Stop", command=check_entry)
stop.pack()

# Has to be at the end of code
window.mainloop()