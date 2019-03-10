'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    dividend = int(input("enter dividend: "))

except ValueError as ve:
    print(f"Please use numerical numbers")

else:
    try:
        divisor = int(input("enter divisor"))

    except ValueError as ve:
        print(f"Please use numerical numbers: ")

    else:
        try:
            print(dividend / divisor)

        except ZeroDivisionError as zde:
            print(f"You can't divide by zero!!")



