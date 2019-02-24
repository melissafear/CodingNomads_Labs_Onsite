'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

miles_to_drive = int(input("Please enter the following\r\nmiles to drive: "))
mpg = int(input("MPG of the car: "))
price_p_gallon= int(input("Price per gallon of fuel: "))

print(f"Cost of Trip = ${miles_to_drive/mpg*price_p_gallon}")