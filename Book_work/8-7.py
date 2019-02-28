# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album


def make_album(artist_name, album_title, tracks = 0):
    my_dict={}
    my_dict[artist_name] = album_title
    if tracks > 0:
        my_dict["tracks" ] = tracks
    return my_dict




album1 = make_album("madonna", "ray of light", 12)
album2 = make_album("U2", "Rattle and something", 10)
album3 = make_album("Lorde", "Melodrama")

print(album1)
print(album2)
print(album3)

#max function??
