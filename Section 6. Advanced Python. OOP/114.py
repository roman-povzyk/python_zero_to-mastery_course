# OOP
class PlayerCharacters:
    membership = True
    def __init__(self, name='anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacters('Cindy', 44)
player2 = PlayerCharacters('Mindy', 21)

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player2.shout())

print(player1.membership)
print(player2.membership)
