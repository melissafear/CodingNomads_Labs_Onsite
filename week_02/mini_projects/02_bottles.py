'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''
vessel="bottles"

for i in range(100,0,-1):

    print(f"{i} {vessel} of beer on the wall,\r\n{i} {vessel} of beer.\r\nTake one down and pass it around, ")

    i=i-1
    if i == 1:
        vessel = "bottle"
    else:
        vessel = "bottles"

    print(f"{i} {vessel} of beer on the wall.\r\n")

#Not complete