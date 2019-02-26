glossary = {"float":"number with decimals", "integer":"number with no decimals", "string":"a bunch of characters", "list":"a bunch of things", "dictionary":"this thing"}

for items in glossary: #(defaults to .keys()
    print(items)

for items in glossary.items():
    print(items)

for k,v in glossary.items():
    print(k, v)
