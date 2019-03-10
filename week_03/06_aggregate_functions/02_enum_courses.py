'''
User python's built-in .enumerate() function to print the classes
together with their numbers from 1-4.


NOTE: a less readable, but common structure in other languages would be:

for i in range(len(courses)):
    print(f"{i}: {courses[i]} python")

'''

classes = ['Intro', 'Intermediate', 'Advanced', 'Epic Hero']

for i, z in enumerate(classes):
    print(f"{i}: {z} python")

for i in range(len(classes)):
    print(f"{i}: {classes[i]}")


print(list(enumerate(classes, 1)))