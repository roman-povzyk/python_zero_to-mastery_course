class User:
    def __init__(self, email):
        self.email = email
        print('init complete')

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack():
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, number_of_arrows):
        self.name = name
        self.power = number_of_arrows

    def check_arrows(self):
        print(f'attacking with arrows: arrows left — {self.number_of_arrows}')

    def run(self):
        print('run really fast!')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, number_of_arrows)
        Archer.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.check_arrows())