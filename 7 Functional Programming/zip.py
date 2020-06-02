#zip function
my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = [7, 9, 11]
print(list(zip(my_list, your_list)))
print(list(zip(your_list, my_list, their_list)))
print(my_list)

'''
grabs the first item from each list and zips them together
'''