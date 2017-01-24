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
btn = Button(root,                  #родительское окно
             text="Сгенерировать",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", gen)       #при нажатии ЛКМ на кнопку вызывается функция gen
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()
