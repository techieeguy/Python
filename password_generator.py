from tkinter import *
import string
import pyperclip
import random

root = Tk()
root.title('Password Generator')
root.geometry("500x500")

passstr = StringVar()
passlen = IntVar()
passlen.set(8)

def generate():
    all_char = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(all_char)
    passstr.set(password)

def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Password Generator", font="calibri 40 bold").pack()
Label(root, text="Enter password length", font="calibri 25").pack(pady=3)
Entry(root,font="calibri 25", textvariable=passlen).pack(pady=3)

Button(root, text="Generate Password", font="calibri 15", command=generate).pack(pady=7)

Entry(root,font="calibri 25", textvariable=passstr).pack(pady=5)

Button(root, text="Copy to clipboard", font="calibri 15", command=copytoclipboard).pack()

root.mainloop()