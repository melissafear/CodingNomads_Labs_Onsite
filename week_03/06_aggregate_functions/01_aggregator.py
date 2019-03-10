'''
Build a simple aggregator function.

'''
list = [1, 2, 3, 4, 5, 6, ]


# the following functions do the same thing

print(sum(list))

def addstuff(item):
    val = 0
    for i in item:
        val += i
    print(val)

addstuff(list)

