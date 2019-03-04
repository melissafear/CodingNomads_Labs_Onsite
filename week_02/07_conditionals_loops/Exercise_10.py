'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''
lower = int(input("type a number "))
upper = int(input ("type a higher number ")) + 1

for num in range(lower, upper):
    print(num ** 2)