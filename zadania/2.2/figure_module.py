from math import pi

class Figure:
    def __init__(self):
        self.color = (123,150,244)
        self.is_filled = False
    
    def __str__(self):
        return 'Color r:{0[0]} g:{0[1]} b:{0[2]} | Filled: {1}'.format(self.color, self.is_filled)

    def __repr__(self):
        params = '('
        for k,v in self.__dict__.items():
            params += f'{k}={v},'
        params = params[:-1] + ')'
        return f'{__name__}.{self.__class__.__name__}{params}'
        
class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def __str__(self):
        return super().__str__() + '\nPromien: {0}'.format(self.radius)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else: 
            print('Promień musi być liczbą dodatnią') 

    @property
    def area(self):
        return pi * self.radius ** 2
    
    @property
    def permiter(self):
        return 1

    @property
    def diameter(self):
        return 2

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def __str__(self):
        return super().__str__() + '\nSzerokosc: {0} Wysokość: {1}'.format(self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width > 0:
            self.__width = width
        else: 
            print('Szerokosc musi być liczbą dodatnią') 

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0:
            self.__height = height
        else: 
            print('Wysokość musi być liczbą dodatnią') 


    @property
    def area(self):
        return self.width * self.height
    
    @property
    def permiter(self):
        return 2 * self.width + 2 * self.height

    @property
    def diagonal(self):
        return 2

if __name__ == "__main__":
    f = Figure()
    print(f)
    print(repr(f))

    c = Circle(5)
    print(c)
    print(repr(c))

    r = Rectangle(10,20)
    print(r)
    print(repr(r))