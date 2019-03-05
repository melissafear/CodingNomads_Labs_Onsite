'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
with open('words.txt', 'r') as fileobject:
    words = fileobject.read()
wordlist = words.split()


print(sorted(wordlist, key=len))
print(min(wordlist, key=len))
print(max(wordlist, key=len))
print(len(wordlist))