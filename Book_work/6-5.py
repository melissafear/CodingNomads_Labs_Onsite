# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.



river_dict = {"Nile":"Egypt", "Waikato": "New Zealand", "Misssissippi":"the USA"}


for river in river_dict.keys():
    print(river)

for river, country in river_dict.items():
    print(river)

for country in river_dict.values():
    print(country)

for river, country in river_dict.items():
    print(f"the {river} river runs through {country}")
