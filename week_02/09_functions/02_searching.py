'''
Write a function that takes in a list and finds the max, min, average and sum.

'''
my_list = [1, 2, 3, 4, 5, 6]


def max_min_avg_sum(list_):
    sum = 0
    for num in list_:
        sum += num

    average = sum/len(list_)
    max_ = max(list_)
    min_ = min(list_)

    return average, sum, max_, min_

print(max_min_avg_sum(my_list))
