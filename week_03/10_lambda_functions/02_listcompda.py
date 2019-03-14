'''
Re-write the following listcomp as a lambda expression.

# names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
# print([x.startswith('D') for x in names])

'''


starts_with_list = lambda letter, my_list : print([x.startswith(letter) for x in my_list])

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

starts_with_list("D", names)
