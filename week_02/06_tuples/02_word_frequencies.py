'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.


'''
from operator import itemgetter


string_ = 'hello here is some'
dict_ = {}
for char in string_:
    if char in dict_:
        dict_[char] += 1
    else:
        dict_[char] = 1

new_list= sorted(dict_.items(), key=itemgetter(1), reverse=True)


for tup in new_list:
    print(tup[0], end = ", ")