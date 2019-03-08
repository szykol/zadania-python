class Smartphone:
    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f'{self.__manufacturer} {self.__model} za jedyne {self.__price}zł'
    
smartphones = [
    Smartphone('Samsung', 'S10', 3900),
    Smartphone('Iphone', 'Jakistam', 0),
    Smartphone('1+', '7', 8),
]

if __name__ == "__main__":
    for sp in smartphones:
        print(sp)

