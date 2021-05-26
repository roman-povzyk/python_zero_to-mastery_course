some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
second_list = []

for i in some_list:
    if some_list.count(i) > 1:
        if i not in second_list:
            second_list.append(i)

print(second_list)
