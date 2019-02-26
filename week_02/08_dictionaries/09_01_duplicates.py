'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''
# count the occurrences of each item and store them in ther dictionary


def has_duplicates(list_):
    my_dict = {}
    for item in my_list:
        if item in my_dict:
            my_dict[item] += 1
            return True
        else:
            my_dict[item] = 1


my_list = [1, 2, 3, 3]

print(has_duplicates(my_list))
