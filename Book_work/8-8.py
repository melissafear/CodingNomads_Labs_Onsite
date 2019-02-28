# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop


def make_album(artist_name, album_title, dict_):
    dict_[artist_name] = album_title
    return dict_

#starts here-----------------

album_input = ""
album_dict = {}

while album_input != "q":
    album_input = input("pls enter an album:  (enter 'quit' to stop): ")
    if album_input =="q":
        break
    artist_input = input("enter an artist: ")

    album_dict = make_album(album_input, artist_input, album_dict)

print(album_dict)

