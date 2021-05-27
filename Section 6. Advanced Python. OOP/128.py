class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack():
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, number_of_arrows):
        self.name = name
        self.power = number_of_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left — {self.number_of_arrows}')

wizard1 = Wizard('Merlin', 60, 'roman@gmail.com')
print(dir(wizard1.email))