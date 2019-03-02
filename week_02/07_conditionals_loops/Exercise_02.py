'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''
days_of_week = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun", "That's not a day of the week!"]

user_input = int(input("pls enter a number and I will tell you the day of the week: "))

print(days_of_week[user_input-1])

# OR

if user_input == 1:
    print("Monday")

elif user_input == 2:
    print("Tuesday")

elif user_input == 3:
    print("Wednesday")

elif user_input == 4:
    print("Thursday")

elif user_input == 5:
    print("Friday")

elif user_input == 6:
    print("Saturday")

elif user_input == 7:
    print("Sunday")

elif user_input >= 8:
    print("That's not a weekday, try again")


