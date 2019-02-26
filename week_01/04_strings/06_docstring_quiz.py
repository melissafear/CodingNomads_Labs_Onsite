'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).



'''

def any_lowercase1(s):
    """ if the first character is lowercase, true will be returned, otherwise false"""
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1("how are things")) #true
print(any_lowercase1("HOW are THINGS")) #false
print(any_lowercase1("hOW ARE THINGS")) #true


def any_lowercase2(s):
    """ this will always return true becuase 'c' is explicitly used and IS lowercase (not sure why it only runs once and not as many times as there are characters in string)"""
    for c in s:
        if 'c'.islower():
            return 'True'
            print(c)
        else:
            return 'False'

print(any_lowercase2("Chow are things"))#true
print(any_lowercase2("cHOW are THINGS"))#true
print(any_lowercase2("chOW ARE THINGS"))#true

def any_lowercase3(s):
    """ will rturn true if all characters are lowercase.  Why can't I return flag?"""
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3("how are things"))#true
print(any_lowercase3("cHOW are THINGS"))#false
print(any_lowercase3("HOW ARE THINGS"))#false


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag



def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


