'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

isinteger = "nope"

while isinteger == "nope":
    user_input = input("pls type a number: ")

    try:
        int(user_input)

    except ValueError as ve:
        print("That was not an integer, try again: ")

    else:
        print("its an integer!")
        isinteger = "yes"
