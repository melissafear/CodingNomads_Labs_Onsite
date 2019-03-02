'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sorted_list = sorted(my_list)

#if list is an uneven number append a 0
length =  len(sorted_list)
if length % 2 == 1:
    sorted_list.append(0)
length =  len(sorted_list)

new_list = []
for i in range(0,length,2 ):
    newtuple = sorted_list[i], sorted_list[i+1]
    new_list.append(newtuple)

print(new_list)



