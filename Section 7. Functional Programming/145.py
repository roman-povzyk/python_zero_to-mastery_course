simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key,value in simple_dict.items()}
print(my_dict)