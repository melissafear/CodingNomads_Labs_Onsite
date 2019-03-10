'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def famous_couples(**couples):
    for k,v in couples.items():
        print(f"{k} and",v)

famous_couples(torville = "dean", peanutbutter = "jelly", romeo = "juliet")
