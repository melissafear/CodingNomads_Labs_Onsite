'''

Building on the dog class from the previous example, create a subclass of the dog class
with at least one additional attribute. Also, override the sleep() and eat() methods to act
slightly different.

Create and object of this class and demonstrate it's functionality.

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
        print(f"{self.name} ate {amount} of {food_item}")
        self.is_hungry = False
        self.percent_full = 100


    def sleep(self):
        time.sleep(.1)
        self.is_hungry = True
        self.percent_full = self.percent_full / 100 * 80

    def __str__(self):
        hungry_status = 'is hungry' if self.is_hungry==True else 'is not hungry'
        return f"{self.name} the dog is {self.color}, {self.age}, is {self.percent_full}% full and {hungry_status}\r\n"


class GiantDog(Dog):
    def __init__(self, name, color, age, percent_full, weight, is_hungry=True):
        super().__init__ (name, color, age, percent_full, is_hungry=True)
        self.weight = weight

    def eat(self, food_item, amount):
        print(f"{self.name} dog ate {amount} {food_item}")
        self.is_hungry = False
        self.percent_full = 95


    def sleep(self):
        time.sleep(.1)
        self.is_hungry = True
        self.percent_full = self.percent_full / 100 * 50

    def __str__(self):
        hungry_status = 'is starving' if self.is_hungry==True else 'is always hungry'
        return f"{self.name} the dog is {self.color}, {self.age}, {self.weight}kgs and {hungry_status}\r\n"


lassie = Dog("Lassie", "white and brown", "about a hundred years old", 100, False)
santas_little_helper = Dog("Santa's little helper", "brown", 10, 50, False)
nana = GiantDog("Nana", "Brown and wears a bonnet", 70, 80, 120, True)

print(nana)
nana.eat("chickens", 2)
print(nana)

print(santas_little_helper)
santas_little_helper.eat("underpants", "2 pairs of")

print(lassie)
lassie.sleep()
lassie.sleep()
lassie.sleep()
lassie.eat("kibble", "1 cup")
print(lassie)