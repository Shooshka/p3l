def printab(a,b):#2 args positional
    print(a)
    print(b)
def printab(a, b=10):#1 arg by default --> printab(5) --> 5, 10 | printab(5,15) --> 5, 15
    print(a)
    print(b)
def printab(a=10, b=10):#2 args by default. printab() --> 10, 10
    print(a)
    print(b)
#incorrect:
def printab(a=10, b):#Error + Нет смысла, т.к. второй аргумент всё равно нужно передавать
    print(a)
    print(b)