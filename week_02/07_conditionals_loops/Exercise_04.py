'''
Print out every prime number between 1 and 100.

'''

# a prime number only has 2 factorials
# a

# for num in range(1, 101):
#     if num > 1:
#         if num % 2 != 0:
#             if num % 3 != 0:
#                 if num % 5 != 0:
#                     if num % 7 != 0:
#                         if num % 11 != 0:
#
#                             print(num)


'''
Print out every prime number between 1 and 100.

'''
for current_num in range(1, 100):
    if current_num > 1:
        for diviser in range (2,current_num):

            if current_num % diviser == 0:
                break
        else:
            print(current_num)




