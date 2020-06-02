#Lists, ordered sequence of objects of any type
#denoted with square brackets

li = [1,2,3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1,2, 'a', True]


#Data structures

amazon_cart = ['notebooks', 'sunglasses', 'tvs']
print(amazon_cart[1])

amazon_cart = ['notebooks', 'sunglasses', 'tvs']
print(amazon_cart[2])

#List slicing
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]
print(amazon_cart) #displays entire list

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]
print(amazon_cart[0::2]) #stepover by 2

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]
print(amazon_cart[::-1])


#we can update the List
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart[0]= 'bikes'
print(new_cart)
print(amazon_cart)

#watch out when copying new lists
amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart #this points to the same memory location for both lists. and changes on new_cart will affect original copy as well
new_cart[0]= 'bikes'
print(new_cart)
print(amazon_cart)

#in order to copy the list, add the brackets

amazon_cart = [
  'notebooks',
  'sunglasses',
  'toys',
  'grapes'
  ]

print('\n')
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] #the brackets ensure a copy, and original does not modify with new_cart
new_cart[0]= 'bikes'
print(new_cart)
print(amazon_cart)

#Matrix, an array, with another array inside. 2D lists, multidimensional list
matrix = [
[1,2,3]
[2,4,6]
[7,8,9]
]

print(matrix[0][1])