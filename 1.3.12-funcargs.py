def printab(a, b, *args):#* - Unlim args
    print('pos arg a -', a)
    print('pos arg b -', b)
    print('all other args :')
    for arg in args:
        print(arg)
printab(10, 20, 30, 40, 50)#a - 10, b - 20, *args - 30,40,50


