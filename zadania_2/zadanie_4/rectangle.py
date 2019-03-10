class Rectangle:
    def __init__(self, length, height):
        try:
            length = float(length)
            height = float(height)
        except ValueError:
            raise InvalidData('Dlugosc boku musi byc liczba')
        else:
            if length <= 0 or height <= 0:
                raise InvalidData('Dlugosc boku nie moze byc ujemna')
            self.height = height
            self.length = length

    def __str__(self):
        return f'a: {self.length} h: {self.height} | area: {self.area()}'

    def __repr__(self):
        return f'{__name__}.{self.__class__.__name__}({self.length},{self.height})'

    def area(self):
        return self.length * self.height
    

class Cuboid(Rectangle):
    def __init__(self, length, height, width):
        super().__init__(length, height)

        try: 
            width = float(width)
        except ValueError:
            raise InvalidData('Dlugosc boku musi byc liczba')
        else:
            if width <= 0:
                raise InvalidData('Dlugosc boku nie moze byc ujemna')
            self.width = width

    def __str__(self):
        prev = super().__str__()
        index = prev.find('|')
        return prev[:index] + f'c: {self.width} ' + prev[index:] + f' volume: {self.volume()}'

    def __repr__(self):
        return f'{__name__}.{self.__class__.__name__}({self.length}, {self.height}, {self.width})'

    def area(self):
        return super().area() * 2 + self.width * self.length * 2 + self.height * self.width * 2

    def volume(self):
        return super().area() * self.width


class InvalidData(Exception):
    pass
    
