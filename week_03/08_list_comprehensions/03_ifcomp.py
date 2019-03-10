'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fishlist= [creature for creature in fish_tuple if "fish" in creature]


print([fishlist])