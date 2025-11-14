from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain):
        self.score=0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label=Label(text=f"Score: {self.score}",fg="White",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")

        self.qtext = self.canvas.create_text(150,125,text="Hi",font=("Arial",20,"italic"),width=280,fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        correct=PhotoImage(file="true.png")
        self.c_button = Button(image=correct,highlightthickness=0,command=self.true)
        self.c_button.grid(row=2,column=0)

        wrong = PhotoImage(file="false.png")
        self.w_button = Button(image=wrong,highlightthickness=0,command=self.false)
        self.w_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.qtext,text=q_text)
        else:
            self.window.destroy()

    def true(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)

    def false(self):
        is_right=self.quiz.check_answer("False")
        self.feedback(is_right)
    def feedback(self,is_right):
        self.window.after(1000,func=self.get_next_question)
        if is_right:
            self.score+=1
            self.canvas.config(bg="Green")
            self.label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")





