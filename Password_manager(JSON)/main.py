from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for i in range(nr_letters) ]
    password_list += [random.choice(symbols) for j in range(nr_symbols)]
    password_list += [random.choice(numbers) for k in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    pwd_int.insert(END,password)

# ---------------------------- SEARCH COMMAND ------------------------------ #
def search_file():
    w_i = web_int.get()
    try:
        with open("Data.json","r") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="File not Found",message="The given file is not found!")
    else:
        if w_i in data:
            messagebox.showinfo(title=w_i, message=f"Email:{data[w_i]["Email"]}\nPassword:{data[w_i]["Password"]}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no details for {w_i}.")



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w_i = web_int.get()
    e_i = mail_int.get()
    pd = pwd_int.get()

    new_data = {w_i:{
        "Email":e_i,
        "Password":pd
    }}

    if (len(w_i)!=0) and (len(pd)!=0):
        try:
            with open("Data.json","r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("Data.json","a") as f:
                json.dump(new_data,f,indent = 4)
        else:
            data.update(new_data)
            with open("Data.json","a") as f:
                json.dump(new_data,f,indent = 4)
        finally:
            web_int.delete(0,END)
            pwd_int.delete(0,END)

    else:
        no = messagebox.showinfo(title="Invalid !!", message="The details you entered are invalid!!")


# ---------------------------- UI SETUP ------------------------------- #ba
tk=Tk()
tk.title("Password Manager")
tk.config(padx=10,pady=10)


#creating the canvas
canvas=Canvas(width=200,height=200)

ph = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = ph)
canvas.grid(column=1,row=0)

#creating labels for each input box
website=Label(text="Website",font=("Arial",10,"normal"),width=35)
website.grid(column=0,row=1)
email=Label(text="Email / Username",font=("Arial",10,"normal"))
email.grid(column=0,row=2)
pwd=Label(text="Password",font=("Arial",10,"normal"),width=21)
pwd.grid(column=0,row=3)

#getting the input
web_int = Entry(width=35)
web_int.focus()
w_i = web_int.get()
web_int.grid(column=1,row=1,columnspan=1)

mail_int = Entry(width=35)
e_i = mail_int.get()
mail_int.grid(column=1,row=2,columnspan=1)

pwd_int = Entry(width=33)
pd = pwd_int.get()
pwd_int.grid(column=1,row=3,columnspan=1,)


#Generating the buttons
gen_pwd=Button(text="Generate Password",command=gen_pd)
gen_pwd.grid(column=2,row=3)

add=Button(text="Add",width=36,command=save)
add.grid(column=1,row=4,columnspan=2)

search = Button(text="Search",width=10,command=search_file)
search.grid(column=2,row = 1,columnspan=2)


tk.mainloop()