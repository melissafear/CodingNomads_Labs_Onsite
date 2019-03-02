# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

import datetime


class User():
    def __init__(self, first_name, last_name, dob_year, dob_month, dob_date, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.dob_year = dob_year
        self.dob_month = dob_month
        self.dob_date = dob_date
        self.sex = sex

    def describe(self):
        print(f"Name: {self.first_name} {self.last_name}\r\nSex: {self.sex}\r\nDOB: {self.dob_date}/{self.dob_month}/{self.dob_year}")


andi = User("Andrea", "Fear-Ross", 1975, 5, 13, "Female")

print(andi.describe())