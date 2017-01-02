from secrets import choice, randbelow
import pyperclip
from tkinter import *

def gen(event):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l1, l2 = [], []
    for i in letters:
        l1.append(i)
        l2.append(i.lower())
    pyperclip.copy(choice(l1) + choice(l1) + choice(l1) + choice(l2) + choice(l2) + choice(l2) + choice(l2) + choice(l2) + str(randbelow(9)))

root = Tk()
btn = Button(root,                  #родительское окно
             text="Сгенерировать",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", gen)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()