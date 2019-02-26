# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.

#
# for i in range(1,21):
#     print(i)
#
#
# i = 0
#
# while i < 21:
#     print(i)
#     i += 1

my_list = [1, 2, 3, 4]


for i in range(0, len(my_list), 2):
    print(my_list[i]+1)

