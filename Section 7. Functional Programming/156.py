def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers' + str(err))

print(sum('1', 2))