def b():
    x = 31#set x in b func
    def a():#set a func
        print(x)#print x in a func
    a()#call a func from b
b()#call b from main