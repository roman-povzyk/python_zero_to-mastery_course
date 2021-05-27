some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

other_list = list(set(num for num in some_list if some_list.count(num) > 1))
print(other_list)
