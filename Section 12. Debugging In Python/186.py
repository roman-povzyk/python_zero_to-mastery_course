import re

pattern = re.compile('this')
string = 'search inside of this text please'

print('search' in string)

a = pattern.search(string)
print(a.span())
print(a.start())
print(a.group())
