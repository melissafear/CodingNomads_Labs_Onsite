'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''


#
# userinput = ("type a number and I will give you the square: ")
#
# try:
#     userinput**2
# except:
#


list_ = ["hello world!"]


try:
    print(list_[1])

except IndexError as ee:
    print("Error:\r\n", ee,"\r\nplease check how many items are in your list")

