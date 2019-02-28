'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.

2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.


'''


import time

class Dog():

    def __init__(self, name, color, age, percent_full, is_hungry=True):
        self.name = name
        self.color = color
        self.age = age
        self.is_hungry = is_hungry
        self.is_hungry = is_hungry
        self.percent_full = percent_full


    def bark(self):
        print("bark bark")


    def eat(self, food_item, amount):
        print(f"the dog ate {amount} of {food_item}")
        self.is_hungry = False
        self.percent_full = 100


    def sleep(self):
        time.sleep(.1)
        self.is_hungry = True
        self.percent_full = self.percent_full / 100 * 80

    def __str__(self):
        hungry_status = 'is hungry' if self.is_hungry==True else 'is not hungry'
        return f"{self.name} the dog is {self.color}, {self.age}, and {hungry_status} becuase {self.name} is {self.percent_full}% full"

lassie = Dog("Lassie", "white and brown", "about a hundred years old", 100, False)
santas_little_helper = Dog("Santa's little helper", "brown", 10, 50, False)

lassie.sleep()
lassie.sleep()
lassie.sleep()


print(santas_little_helper)
print(lassie)

lassie.eat("whole chickens", 3)
print(lassie)