import secrets
import pyperclip

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_lst = []
letterssmall_lst = []

for i in letters:
    letters_lst.append(i)
    letterssmall_lst.append(i.lower())
gen = secrets.choice
pwd = gen(letters_lst) + gen(letters_lst) + gen(letters_lst) + gen(letterssmall_lst) + gen(letterssmall_lst) + gen(letterssmall_lst) + gen(letterssmall_lst) + gen(letterssmall_lst) + str(secrets.randbelow(9))
pyperclip.copy(pwd)
