'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!


#https://towardsdatascience.com/introduction-to-web-scraping-with-beautifulsoup-e87a06c2b857
'''
from bs4 import BeautifulSoup
import urllib.request
import re


url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

page = urllib.request.urlopen(url)

# try:
#     page = urllib.request.urlopen(url)
#
# except:
#     print("An error occured.")

soup = BeautifulSoup(page, 'html.parser')
print(soup)