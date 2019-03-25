from Coin import Coin

if __name__ == "__main__":
    coin = Coin()

    for i in range(15):
        coin.throw()
        print(f'Rzut numer {i+1}: {coin.show_side()}')
