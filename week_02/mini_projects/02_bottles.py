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
vessel1 = "bottles"
vessel2 = "bottles"
for i in range(100,0,-1):
    if i == 2:
        vessel1 = "bottle"
    if i == 1:
        print(f"{i} {vessel1} of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} {vessel2} of beer on the wall.\r\n")
        else:
        print(f"{i} {vessel1} of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} {vessel2} of beer on the wall.\r\n")
