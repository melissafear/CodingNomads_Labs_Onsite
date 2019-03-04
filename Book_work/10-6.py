# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.




try:
    user_input1 = int(input("type a number"))

except ValueError as ve:
    print(f"please type a whole numerical number this is a {type(ve)}")
    print(ve)

except ZeroDivisionError as zde:
    print("please type a whole numerical number")
    print(zde)

except Exception as exe:
    print(exe)


try:

    user_input2 = int(input("type another number"))


except ValueError as ve:
    print(f"please type a whole numerical number this is a {type(ve)}")
    print(ve)

except ZeroDivisionError as zde:
    print("please type a whole numerical number")
    print(zde)

except Exception as exe:
    print(exe)

print(user_input1+user_input2)
