# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.


user_input = ""
filename = "I_heart_programming.txt"

while user_input != "q":

    user_input = input("why you love programming? ")

    with open(filename, 'a') as file_object:
        file_object.write(f"{user_input}\n")