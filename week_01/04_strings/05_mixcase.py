'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''


text = "here is a string of text"

print(text.upper())
print(text.lower())


# OPTION ONE

upper = text.upper()
print(upper.replace("A","a").replace("E","e").replace("I","i").replace("O","o").replace("U","u"))


# OPTION TWO

vowels = ["a", "e", "i", "o", "u"]

for letter in text:
    if letter in vowels:
        text = text.replace(letter,letter.lower())
    if letter not in vowels:
        text = text.replace(letter,letter.upper())

print(text)

