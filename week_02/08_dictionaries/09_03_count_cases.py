'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dicts!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

text = "I love to work with dicts!"

my_dict = {"upper":0, "lower":0, "space":0, "punctuation":0, }

punctuation_chars = "!@#$%^&*()_+:?><,./';[]'"

for char in text:
    if char.isupper() == True:
        my_dict["upper"] += 1

    elif char.islower() == True:
        my_dict["lower"] += 1

    elif char == " ":
        my_dict["space"] += 1

    elif char in punctuation_chars:
        my_dict["punctuation"] += 1


print(my_dict)
