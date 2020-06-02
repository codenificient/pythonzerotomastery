#Range
print(range(1,100))
print(list(range(1, 100)))

print(list(range(100)))

#Join, string method
sentence = '!'
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Christian'])
print(new_sentence)

#clean it up
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Christian'])
print(new_sentence)

#clean it up even more

new_sentence = ' '.join(['Hi,', 'my', 'name', 'is', 'Christian'])
print(new_sentence)