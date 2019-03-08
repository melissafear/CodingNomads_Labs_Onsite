'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

#wordslist = ["h","e","l","l","o"]
with open('words.txt', 'r') as fileobject:
    words = fileobject.read()
    wordslist = words.split()

wordslist.reverse()
print(wordslist)

with open('words_reverse.txt', 'w') as newfileobject:
    for word in wordslist:
        newfileobject.write(f"{word}\r\n")

