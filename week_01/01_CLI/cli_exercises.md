# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
- Move into the CodingNomads folder
- Create new folder cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    c. list the contents of the folder
    d. rename one of the files
- Inside of folder cli_testing, create a new folder
- Copy a file from cli_testing to the new folder
- Move a different file from cli_testing to the new folder
- Demonstrate removing:
    a. A file
    b. A folder


## vim

- Use `$ vim` to write some text inside a file
- Use `$ cat` print contents of file
- Use `$ grep` to search for a word inside file


## explore advanced CLI

- What is the difference between the two commands > and >>?
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
- Overwrite the content of my_file.txt with "tell me"



THMB:labs_onsite melissa$ cd ~
THMB:~ melissa$ pwd
/Users/melissa
THMB:~ melissa$ mkdir CodingNomads
THMB:~ melissa$ cd CodingNomads/
THMB:CodingNomads melissa$ mkdir cli_testing
THMB:CodingNomads melissa$ ls
cli_testing
THMB:CodingNomads melissa$ cd cli_testing/
THMB:cli_testing melissa$ touch file1.txt, file2.txt file3.txt
THMB:cli_testing melissa$ ls
file1.txt,	file2.txt	file3.txt
THMB:cli_testing melissa$ mv file1.txt, file01.txt
THMB:cli_testing melissa$ ls
file01.txt	file2.txt	file3.txt
THMB:cli_testing melissa$ mkdir newerfolder
THMB:cli_testing melissa$ mv file01.txt /Users/melissa/CodingNomads/cli_testing/newerfolder
THMB:cli_testing melissa$ cp file2.txt /Users/melissa/CodingNomads/cli_testing/newerfolder
THMB:cli_testing melissa$ ls
file2.txt	file3.txt	newerfolder
THMB:cli_testing melissa$ cd newerfolder
THMB:newerfolder melissa$ ls
file01.txt	file2.txt
THMB:newerfolder melissa$ cd ..
THMB:cli_testing melissa$ ls
file2.txt	file3.txt	newerfolder
THMB:cli_testing melissa$ rm file3.txt
THMB:cli_testing melissa$ rm -r newerfolder
THMB:cli_testing melissa$ ls
file2.txt