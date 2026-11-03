from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_Sec=LONG_BREAK_MIN*60
    if reps%8==0:
        count_down(long_break_Sec)
        title_Label.config(text="Timer",fg=PINK,bg=PINK,font=(FONT_NAME,100))

    elif reps&2==0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)

def count_down(count):
      
    minutes=count//60
    seconds=count%60
    if seconds<10:
        seconds=f"0{seconds}"
    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count>0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()


window=Tk()
window.title("Title")
window.config(padx=100,pady=50,bg=YELLOW)

title_Label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_Label.grid(column=1,row=0)

tomato_image=PhotoImage(file="tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(column=1,row=1)


start_button=Button(text="Start",bg=YELLOW,command=start_timer)
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset",bg=YELLOW)
reset_button.grid(column=2,row=2)
window.mainloop()