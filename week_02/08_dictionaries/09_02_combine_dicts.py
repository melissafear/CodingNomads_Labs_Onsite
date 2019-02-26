'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''

dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

'''makes a copy of dict_1'''
dict_4 = dict(dict_1)

'''appends dict 2 & 3 to dict 4'''
dict_4.update(dict_2)
dict_4.update(dict_3)


print(dict_4)