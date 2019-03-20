'''
Write a script that connects to the http://numbersapi.com/ and fetches trivia on all
numbers from 0 through 100.

Store the responses in a new JSON file called numbers.json

BONUS:
* fetch information of all the prime numbers from 1-1000
* cycle through the different endpoints the API provides (trivia, math, date, year)
  in a way that they change in binary chunks, e.g.:
  - the info on the first 2 numbers are of type trivia
  - info on the next 4 numbers are of type math
  - the next 8 are on dates
  - etc. (cycle back to the trivia after year)

'''

import requests
num = 0
trivia_dict = {}
for i in range(0,3):
    url = 'http://numbersapi.com/'+ str(num)+'/trivia?fragment'
    trivia = requests.get(url)
    print(trivia.text)
    num += 1
    trivia_dict[num]=trivia.text

with open('numbers.json', 'w') as fout:
    numbers_json = fout.write(str(trivia_dict))


