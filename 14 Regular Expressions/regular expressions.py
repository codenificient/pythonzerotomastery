import re
string = 'search this inside of this text please'
print('search' in string)

print(re.search('this', string))
a = re.search('this', string)
print(a.span())
print(a.group())
print(a.end())
print(a.start())

pattern = re.compile('this')

print(pattern.search(string))
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(b)
print(c)
print(d)