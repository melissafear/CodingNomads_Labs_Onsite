'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(iterable):
    list_ = []
    counter = -1
    for i in iterable:
        counter +=1
        tuple_ = counter, iterable[counter]
        list_.append(tuple_)
    return list_



classes = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

print(my_enumerate(classes))

#print(list(enumerate(classes)))



