# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.


numbers = {"Tim":20, "Sam":5, "Faith":1000, "Pat":12, "Melissa":13}

for key in numbers:
    print(f"{key} : {numbers[key]}")

#OR

print(numbers.items())

