'''
Write a script with a function that demonstrates the use of *args.

'''



def amazing_sandwich_fillings(*fillings):
    return print(*fillings)

amazing_sandwich_fillings("bacon", "lettuce", "tomato")