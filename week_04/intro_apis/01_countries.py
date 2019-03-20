'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests

url3 = 'https://restcountries.eu/rest/v2/all'
list_ = requests.get(url3)
list_json = list_.json()

print("Enter:")
index = 0
for item in list_json:
    print(f"{list_json[index]['alpha2Code']} for {list_json[index]['name']}")
    index += 1


countries = input("type 2 country codes separated by a comma: ")

cntry1 = countries[0:2]
cntry2 = countries[4:6]

url1 = f'https://restcountries.eu/rest/v2/alpha/{cntry1}'
url2 = f'https://restcountries.eu/rest/v2/alpha/{cntry2}'

country1 = requests.get(url1)
country1_json = country1.json()

country2 = requests.get(url2)
country2_json = country2.json()

name1 = country1_json["name"]
pop1 = country1_json["population"]
print(f"{name1} has a population of {pop1}")

name2 = country2_json["name"]
pop2 = country2_json["population"]
print(f"{name2} has a population of {pop2}")




