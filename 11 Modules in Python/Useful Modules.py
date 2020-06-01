from  collections import Counter, defaultdict, OrderedDict
li = [2, 3, 4, 5, 6, 3, 6, 6, 3, 7]
print(Counter(li))

sentence = ' blah blah blah thinking about python this spring '
new_sen = sentence.strip()
print(Counter(sentence))
print(new_sen)

dicton = defaultdict(lambda : 'does not exist', {'a':1, 'b': 2})
print(dicton['a'])

d = OrderedDict()
d['a'] = 1
d['b']= 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print(d2 == d) #false due to wrong order

#correct order
d3 = OrderedDict()
d3['b'] = 2
d3['a'] = 1

d4= OrderedDict()
d4['b'] = 2
d4['a'] = 1
print(d3 == d4) #True