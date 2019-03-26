import math
import sys

def pierwsze():
    liczba = 2
    while True:
        if jest_pierwsza(liczba):
            yield liczba
        liczba += 1

def jest_pierwsza(l):
    for i in range(2, int(math.sqrt(l)) + 1):
        if l % i == 0:
            return False

    return True

with open('liczby_pierwsze.txt', 'w') as f:
    for index, val in enumerate(pierwsze()):
        if index >= 10000:
            sys.exit(0)
        
        f.write(f'{val}\n')




        