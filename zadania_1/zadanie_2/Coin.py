import random

class Coin:
    def __init__(self):
        self.throw()

    def show_side(self):
        return self.side

    def throw(self):
        self.side = 'Orzeł' if random.randint(0, 1) == 0 else 'Reszka'

if __name__ == "__main__":
    coin1 = Coin()
    print(coin1.show_side())
    coin1.throw()
    print(coin1.show_side())
    coin1.throw()
    print(coin1.show_side())

    coin2 = Coin()
    print(coin2.show_side())

    coin3 = Coin()
    print(coin3.show_side())
