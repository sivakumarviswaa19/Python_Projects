from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")
    learn =  data.to_dict(orient="records")
else:
    learn=data.to_dict(orient="records")
card = {}





def next_cards():
    global card
    global flip_time
    tk.after_cancel(flip_time)
    card = random.choice(learn)
    canvas.itemconfig(fr,text="French",fill="black")
    canvas.itemconfig(fr_word,text=card["French"],fill="black")
    canvas.itemconfig(img, image=front_ground)
    flip_time = tk.after(3000, func=flip)


def flip():
    canvas.itemconfig(fr,text="English",fill="white")
    canvas.itemconfig(fr_word,text=card["English"],fill="white")
    canvas.itemconfig(img,image=back_ground)

def known():
    learn.remove(card)
    next_cards()
    data1 = pandas.DataFrame(learn)
    data1.to_csv("words_to_learn.csv")

#UI SETUP
tk = Tk()
tk.title("FlashCards")
tk.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_time=tk.after(3000,func=flip)

front_ground = PhotoImage(file="card_front.png")
canvas=Canvas(height=526,width=800)
back_ground = PhotoImage(file="card_back.png")
img = canvas.create_image(400,263,image=front_ground)
canvas.grid(column=0,row=0,columnspan=2)


#text
fr=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
fr_word=canvas.create_text(400,263,text="trouve",font=("Arial",60,"bold"))


cross = PhotoImage(file="wrong.png")
tick = PhotoImage(file="right.png")

wrong=Button(image=cross,command = next_cards)
wrong.grid(column=0,row = 1)

correct=Button(image=tick,command = known)
correct.grid(column=1,row=1)
next_cards()


tk.mainloop()

