from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7]
print(Counter(li))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(dictionary['b'])

d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = {'c': 100}
d2['a'] = 1
d2['b'] = 2

print(d2 == d)
