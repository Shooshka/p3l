def printab(a, b, **kwargs):#Словарь kwargs
    print('pos arg a -', a)
    print('pos arg b -', b)
    print('additional args:')
    for key in kwargs:
        print(key, kwargs[key])
printab(10, 20, c=30, d=40, jimmi=123)#a - 10, b - 20, jimmi 123, c 30, d 40 - **kwargs