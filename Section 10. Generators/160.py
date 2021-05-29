def generator_function(num):
    for i in range(num):
        yield i * 2


g = generator_function(100)
print(g)

# for item in generator_function(1000):
#     print(item)
