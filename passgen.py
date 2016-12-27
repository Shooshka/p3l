from secrets import choice, randbelow
import pyperclip

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l1, l2 = [], []

for i in letters:
    l1.append(i)
    l2.append(i.lower())
pyperclip.copy(choice(l1) + choice(l1) + choice(l1) + choice(l2) + choice(l2) + choice(l2) + choice(l2) + choice(l2) + str(randbelow(9)))
