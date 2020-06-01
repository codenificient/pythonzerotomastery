import re

pattern = re.compile(r"([a-z A-Z]).([a])")
string = 'search this inside of this text please! lorena'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a)
print(b)
print(c)
print(d)
print(a.group(1))