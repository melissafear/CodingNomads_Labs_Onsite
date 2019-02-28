nested_list = [1, 1, 1, [2, 2, [3, [4, 4 ]],2, 2, ],1, ]
flat_list = []

def unpack_list(nested_list):
    for item in nested_list:
        if type(item) ==list:
            unpack_list(item)
        else:
            flat_list.append(item)
    return

unpack_list(nested_list)
print(flat_list)