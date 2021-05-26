def highest_even(li):
    max = 0
    for i in li:
        if i % 2 == 0:
            if i > max:
                max = i
    return max


print(highest_even([10, 2, 3, 4, 8, 11]))
