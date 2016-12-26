ok_status = True#global var
vowels = ['a', 'u', 'i', 'e', 'o']

def check(word):
    global ok_status#use global var!
    for vowel in vowels:
        if vowel in word:
            return True
    ok_status = False
    return False
print(check('abcacba'))
print(ok_status)
print(check('www'))
print(ok_status)