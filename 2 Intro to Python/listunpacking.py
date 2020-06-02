#list Unpacking
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

#unpacking1
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8]
print(a, b, c)
print(other)

#unpacking2
a, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(other)
print(d)

#None
weapons = None
print(weapons)