t_c = 18#global var
tmp = 'ok'#tmp - global var

def fahrenheit(t_c):
    tmp = t_c * 9 / 5#tmp - local var
    return tmp + 32
print(fahrenheit(t_c))#--> 64.4
print(tmp) #--> ok