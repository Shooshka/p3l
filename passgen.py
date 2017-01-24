from secrets import choice
import string
import pyperclip
from tkinter import Tk, Button

def gen(event):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(choice(alphabet) for i in range(8))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 1):
            break
    pyperclip.copy(password)

root = Tk()
btn = Button(root,
             text="Сгенерировать",
             width=30,height=5,
             bg="white",fg="black")
btn.bind("<Button-1>", gen)
btn.pack()
root.mainloop()
