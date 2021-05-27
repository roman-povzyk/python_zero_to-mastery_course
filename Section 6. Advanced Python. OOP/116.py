# OOP
class PlayerCharacters:
    membership = True
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# player1 = PlayerCharacters('Tom', 10)
player3 = PlayerCharacters.adding_things(2, 3)
print(player3.age)
