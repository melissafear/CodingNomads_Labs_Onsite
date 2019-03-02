'''
Demonstrate the use of the "break" statement to exit a loop.

'''

letter = 'o'
str = "this is some text"

for i in str:
    if i == letter:
        break
    else:
        print(i)