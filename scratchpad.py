books = [book1.txt, book2.txt]

for book in books:
    try:
        with open(book, "r") as fin:
            content = fin.read()
    except FileNotFoundError as fnf:
        print(fnf)
    except PermissionError as err:
        print(err)
    else:
        print(first_char)

