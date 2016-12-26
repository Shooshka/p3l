def printab(a,b):
    print(a)
    print(b)

#Correct calls
printab(10, 20)
printab(a=10, b=20)
printab(b=20, a=10)
#Keyword args always first!
printab(10, b=20)

lst = [10, 20]
printab(*lst) #Same as printab(lst[0], lst[1])

args = {'a' : 10, 'b' : 20}
printab(**args) #Same as printab(key1 = args[key1], key2 = args[key2])#printab(args['a'], args['b'])
