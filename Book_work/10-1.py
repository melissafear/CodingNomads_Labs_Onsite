# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can.... Save the file as learning_python.txt in the
# same directory as your exercises from this chapter. Write a program that reads
# the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping
# over the file object, and once by storing
# the lines in a list and then working with them outside the with block.


with open('learningpython.txt', 'r') as fin:
    lp = fin.read()
print(lp*3)


with open('learningpython.txt', 'r') as fin:
    lpl = fin.readlines()
    for line in lpl:
        print(line)


print(lpl[0]*10)
