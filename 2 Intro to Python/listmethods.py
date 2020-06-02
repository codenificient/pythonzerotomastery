#List Methods
#len
basket = [1,2, 3, 4, 5]
print(len(basket))

#adding
basket = [1,2, 3, 4, 5]
new_list = basket.append(100)
print(basket)
print(new_list) #will return None, but append modifies list in place


#in order to print new list, redifine new list
basket = [1, 2, 3, 4, 5]
basket.append(100)
new_list = basket
print(basket)
print(new_list)

print('\n')
#insert
basket = [1, 2, 3, 4, 5]
basket.insert(3, 120)
print(basket)
print(new_list)
print('\n')
#can also use insert directly
basket1 = [1, 2, 3, 4, 5]
basket1.insert(3, 130)
print(basket1)

#Removing 
basket = [1,2, 3, 4, 5]
basket.pop()
print(basket) #removes whatever is at the end of list


print(basket.pop(0)) #removes index of zero, will return the value removed

#actual Remove

basket = [1,2, 3, 4, 5]
basket.remove(4) #we give the value we want removed
print(basket) #modifies the list in place


#remove will elimate a value, pop will remove the value at the index, and return the value

#clear 
basket = [1,2, 3, 4, 5]
basket.clear()
print(basket) #clears all the values in basket, returns empty list

#index
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('c'))

#range lookup
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('c', 0, 3)) #will look for value of 'c' from index of 0 and stop right before index of 3. #Will not find 'c' and will give error message if 'c' in not in that range

basket = ['a', 'b', 'd', 'c', 'e']
print(basket.index('c', 0, 5))

#practice booleans 
#the in method helps you find the needle in digital haystack of big data
print('x' in 'xristian') #painfully obvious

print('i' in 'teamwork') #good luck with that

print('\n')

#Sort
basket = ['a', 'b', 'c', 'e', 'd']
basket.sort()
print(basket)

#sorted
basket = ['a', 'b', 'c', 'e', 'x', 'd']
print(sorted(basket)) #new copy of basket data, then sorted
print(basket)

print('\n')

#expanding the Sorted method
basket = ['a', 'b', 'c', 'e', 'x', 'd']
new_basket = basket[:]
new_basket.sort()
print(new_basket)

#copy method, same as expanded
basket = ['a', 'b', 'c', 'e', 'x', 'd']
new_basket = basket.copy()
new_basket.sort()
print(new_basket)

#Reverse
basket = ['a', 'b', 'c', 'e', 'x', 'd']
basket.reverse()
print(basket)

#Sorted, Reverse
basket = ['a', 'b', 'c', 'e', 'x', 'd']
basket.sort()
basket.reverse()
print(basket)

#Reverse, Sorted
basket = ['a', 'b', 'c', 'e', 'x', 'd']
basket.reverse()
basket.sort()
print(basket)

#adding Slicing to the mix
basket = ['a', 'b', 'c', 'e', 'x', 'd']
basket.sort()
basket.reverse()
print(basket[::-1]) #sorted copy of the reversed list
print(basket) #original reversed list