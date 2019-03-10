'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
with open('words.txt', 'r') as fileobject:
    words = fileobject.read()
wordlist = words.split()

min_length = len(min(wordlist, key=len))
max_length = len(max(wordlist, key=len))

print(max_length)

for word in wordlist:
    if len(word) == min_length:
        print(word)

for word in wordlist:
    if len(word) == max_length:
        print(word)


print(f"\n{len(wordlist)}")
