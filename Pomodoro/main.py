from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
count = 1
cont= 0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    canvas.after_cancel()
    canvas.itemconfig(time,text="00:00")
    canvas.itemconfig(content,text="Timer")
    check = ""
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    if reps %2 == 0 and reps !=8:
        canvas.itemconfig(content, text="Short Break",font=(FONT_NAME,20,"bold"),fill=PINK)
        count = SHORT_BREAK_MIN * 60
        timer(count)

    elif reps%2 != 0 :
        canvas.itemconfig(content, text="Work Time",font=(FONT_NAME,25,"bold"))
        count = WORK_MIN * 60
        timer(count)
    else:
        canvas.itemconfig(content, text="Long Break",font=(FONT_NAME,20,"bold"),fill=RED)
        count=LONG_BREAK_MIN * 60
        timer(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer(count):
    min=math.floor(count/60)
    sec=count%60
    if sec == 0:
        sec = "00"
    ls=[1,2,3,4,5,6,7,8,9]
    if sec in ls:
        sec = "0"+str(sec)

    canvas.itemconfig(time,text=f"{min}:{sec}",font=(FONT_NAME,20,"bold"))

    if count > 0:
        canvas.after(1000,timer,count - 1,)
    else:
        if reps %2 != 0:
            reset_clicked()


        start_time()
# ---------------------------- UI SETUP ------------------------------- #
tk = Tk()
tk.title("Pomodoro !")
tk.config(padx=100,pady=100,bg=YELLOW)


canvas = Canvas(width=200,height=300,bg=YELLOW,highlightthickness=0)
tomato = PhotoImage(file = "tomato.png")

check = ""
ch_mark = Label(text=check,bg=GREEN,highlightthickness =0 )
ch_mark.grid(column=2,row=9) 


def reset_clicked():
    global cont
    cont +=1
    check = cont * "✓"

    ch_mark.config(text=check)



start=Button(text="Start",width=5,highlightthickness=0,command=start_time)
start.grid(column=1,row=9)

reset=Button(text="Reset",width=5,highlightthickness=0,command=reset_clicked)
reset.grid(column=3,row=9)



canvas.create_image(100,140,image=tomato)
time = canvas.create_text(103,158,fill = "white",text="00:00",font=(FONT_NAME,20,"bold"))
content = canvas.create_text(103,15,fill=GREEN,text="Timer",font=(FONT_NAME,30,"bold"))
canvas.grid(column=2,row=2)

tk.mainloop()