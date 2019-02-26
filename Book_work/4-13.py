# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

buffet = ("pasta", "chicken", "salad", "stew", "soup")


for food in buffet:
    print(food)

# #buffet[1] = "beef"
#
# buffet_list = list(buffet)
#
# buffet_list[1] = "beef"
# buffet_list[2] = "vegetables"
#
# buffet = tuple(buffet_list)
#
# print(type(buffet))
# print(buffet)


new_items = ("beef", "vegetables")

buffet = buffet[0:1]+ new_items + buffet[3:5]

print(buffet)

