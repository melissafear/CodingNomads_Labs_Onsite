'''
Write a script that finds the first vowel in a a user inputted string.

'''

vowels = ["a", "e", "i", "o", "u"]

text = input("write some words and I will give you the first vowel: ").lower()

# for vowel in vowels:
#     print(text.find(vowel))

for letter in text:
    if letter in vowels:
        print(letter)
        break