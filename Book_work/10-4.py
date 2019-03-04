# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

user_input = ""
filename = "guest_book.txt"

while user_input != "q":
    user_input = input("please type your name: ")
    if user_input== 'q':
        break
    else:

        print(f"hello {user_input}")

    with open(filename, 'a') as file_object:
        file_object.write(f"{user_input}\n")


