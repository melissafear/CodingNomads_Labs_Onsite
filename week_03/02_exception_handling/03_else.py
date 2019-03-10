'''
Write a script that demonstrates a try/except/else.

'''

try:
    userinput = int(input("number pls: "))

except ValueError as ve:
    print(f"Please use a number")

else:
    print(userinput**2)