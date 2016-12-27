import pyperclip
import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_lst = []
letterssmall_lst = []

for i in letters:
    letters_lst.append(i)
    letterssmall_lst.append(i.lower())

pwd = random.choice(letters_lst) + random.choice(letters_lst) + random.choice(letters_lst) + random.choice(letterssmall_lst) + random.choice(letterssmall_lst) + random.choice(letterssmall_lst) + random.choice(letterssmall_lst) + random.choice(letterssmall_lst) + str(random.randint(0,9))
pyperclip.copy(pwd)