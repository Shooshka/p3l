class MyClass:
    a = 10

    def func():
        print('Hello')

print(MyClass.a)
print(MyClass.func())

x = MyClass()
print(type(x))
print(type(MyClass))