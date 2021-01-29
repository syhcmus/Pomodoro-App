from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer

    reps -= 1
    title_label.config(text="Timer")    
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, timer
    if timer != None:
        window.after_cancel(timer)
        timer = None    
    

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break", fg=RED)
        reps = 1
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break", fg=PINK)    
    else:
        count_down(WORK_MIN)
        title_label.config(text="Work", fg=GREEN)

    reps += 1

    
        
    
    
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(minute, second = 0):
    global timer
    
    if minute >= 0:
        time = f"{minute}: {second}"
        if second < 10:
            time = f"{minute}: 0{second}"
        canvas.itemconfig(timer_text, text=time)
        second -= 1
        if second < 0:
            minute -= 1
            second = 59
        
        timer = window.after(1000, count_down, minute, second)
    else:
        start_timer()
    
        
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


window.after(1000, )

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()