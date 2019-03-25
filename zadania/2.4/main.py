from rectangle import Rectangle, Cuboid, InvalidData

if __name__ == "__main__":
    try:
        with open('zadanie_4/dane.txt', 'r') as f:
            for line in f:
                inputs = line.split()
                try:
                    length, height = inputs[1], inputs[2]
                    if inputs[0] == '1':
                        r = Rectangle(length, height)
                        print(r)
                    elif inputs[0] == '2':
                        width = inputs[3]
                        c = Cuboid(length, height, width)
                        print(c)
                except InvalidData as e:
                    print(e)
                except IndexError as e:
                    print('Podano nieprawidlowa ilosc bokow')

    except FileNotFoundError as e:
        print(e)
                    
