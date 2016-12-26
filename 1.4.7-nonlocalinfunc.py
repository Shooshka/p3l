def f():
    ok_status = True#local f namespace
    vowels = ['a', 'u', 'i', 'e', 'o']

    def check(word):
        nonlocal ok_status  # use non-local var and not global var!
        for vowel in vowels:
            if vowel in word:
                return True
        ok_status = False
        return False
    print(check('abcacba'))
    print(ok_status)
    print(check('www'))
    print(ok_status)
f()
print(ok_status)#Error! No global var!