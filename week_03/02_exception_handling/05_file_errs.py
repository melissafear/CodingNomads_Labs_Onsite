'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
try:
    with open("integers.txt", "r") as fileobject:
        line1 = fileobject.readline()

except FileNotFoundError:
    print("This file does not exist")

else:


    try:
        line1 = int(line1)
        calc = line1/line1


    except ValueError as ve:
        print(ve,"\r\n Not a number")

    except TypeError as te:
        print(" Not a number\r\n",te)


    else:
        print(calc)