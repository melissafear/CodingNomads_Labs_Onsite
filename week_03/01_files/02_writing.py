'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open('words.txt', 'r') as fileobject:
    words = fileobject.read()
    wordslist = words.split()


wordslist.sort(reverse=True)
print(wordslist)
