'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
#File Setup
with open('file_with_words.txt', 'w') as file_object:
    file_object.write(f"she sells seashells by the sea shore")

#-------------------------------------------------

def sed(pattern, replacement, file1, file2):

    try:
        with open(file1, 'r') as file_object:
            text = file_object.read()

    except FileNotFoundError:
            print(f"{file1} not found")

    else:
        changed_text = text.replace(pattern, replacement)

    try:
        with open(file2, 'w') as file_object2:
          file_object2.write(changed_text)

    except: #FileNotFoundError:
        pass #whats a good exception for this?
    #https://docs.python.org/3/library/exceptions.html#bltin-exceptions


sed("sh", "sc", "file_with_words.txt", "file_with_altered_wordss.txt")

