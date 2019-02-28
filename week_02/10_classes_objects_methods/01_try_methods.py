'''
We've learned about strings earlier. Looking at string methods from the
perspective of "everything is an object in python" explains the syntax
that we encountered there.

Now take a second look at the documentation of the string methods at:
http://docs.python.org/3/library/stdtypes.html#string-methods.

Demonstrate 3 interesting string methods of your choice and explain why
they are invoked like this: str.method()


'''

str = "Hello There"
print(str.capitalize())
print(str.upper())
print(str.swapcase())


str1 = "34"
str2 = "233"

print(str1.zfill(10))
print(str2.zfill(10))


str3 = "<b>check if this test starts with a bold tag"
print(str3)
print(str3.startswith("<b>",0))
print(str3.replace("<b>", ""))


# methods are invoked this way, because they are part of the class