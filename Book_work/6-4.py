# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.


glossary = {"float":"number with decimals", "integer":"number with no decimals", "string":"a bunch of characters", "list":"a bunch of things", "dictionary":"this thing"}




for items in glossary: #(defaults to .keys()
    print(items)

print(" ")

for items in glossary.items():
    print(items)

print(" ")

for k,v in glossary.items():
    print(k, v)