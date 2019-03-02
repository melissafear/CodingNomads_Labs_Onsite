
'''
Flush out the classes below with the following:

    - Add inheritance so that Class1 is inherited by Class2 and Class2 is inherited by Class3.
    - Follow the directions in each class to complete the functionality.



'''

class Class1():
    def __init__(self, x):
        self.x = x
    # define an __init__() method that sets an attribute x


class Class2(Class1):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    # define an __init__() method that sets an attribute y and calls the __init__() method of its parent

class Class3(Class2):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    # define an __init__() method that sets an attribute z and calls the __init__() method of its parent

thingc1 = Class1("width")
thingc2 = Class2("width", "height")
thingc3 = Class3("width", "height", "depth")

print(thingc1.x)
print(thingc2.x, thingc2.y)
print(thingc3.x, thingc3.y, thingc3.z)



# create an object of each class and print each of its attributes
