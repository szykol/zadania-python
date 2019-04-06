from abc import ABC, abstractmethod

class Temperature(ABC):
    @abstractmethod
    def __init__(self, temperature):
        self.__temperature = temperature

    @abstractmethod
    def _temp_setter(self, temperature):
        self.__temperature = temperature

    def __str__(self):
        return f'{self.temperature} ° w skali Celsjusz'

    def __repr__(self):
        return f'{type(self)(self.temperature)}'

    def above_freezing(self):
        return self.convert_to_Celsius().temperature > 0

    @abstractmethod
    def convert_to_Fahrenheit(self):
        pass

    @abstractmethod
    def convert_to_Celsius(self):
        pass

    @abstractmethod
    def convert_to_Kelvin(self):
        pass

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temp_setter(temperature)

class Celsius(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def _temp_setter(self, temperature):
        self.__temperature = temperature

    def convert_to_Fahrenheit(self):
        return Fahrenheit(self.temperature * 9 / 5 + 32)

    def convert_to_Kelvin(self):
        return Kelvin(self.temperature + 273.15)

    def convert_to_Celsius(self):
        return self

class Kelvin(Temperature): 
    def __init__(self, temperature):
        super().__init__(temperature)

    def _temp_setter(self, temperature):
        self.__temperature = temperature
    
    def convert_to_Fahrenheit(self):
        return Fahrenheit(self.temperature * 9 / 5 - 459.67)

    def convert_to_Kelvin(self):
        return self

    def convert_to_Celsius(self):
        return Celsius(self.temperature  - 273.15)

    
class Fahrenheit(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    def _temp_setter(self, temperature):
        self.__temperature = temperature
    
    def convert_to_Fahrenheit(self):
        return self

    def convert_to_Kelvin(self):
        return Kelvin((self.temperature + 459.67) * 5 / 9)

    def convert_to_Celsius(self):
        return Celsius((self.temperature - 32) * 5 / 9)

if __name__ == "__main__":
    temps = [
        Kelvin(100),
        Kelvin(50),
        Kelvin(30),

        Celsius(-5),
        Celsius(15),
        Celsius(0),

        Fahrenheit(200),
        Fahrenheit(-200),
        Fahrenheit(0)
    ]

    for temp in temps:
        out = str(temp)
        if temp.above_freezing():
            out += ' Powyżej zera'
        print(out)

    kelvinTemps = [temp.convert_to_Kelvin() for temp in temps]
    celsiusTemps = [temp.convert_to_Celsius() for temp in temps]
    fahrenTemps = [temp.convert_to_Fahrenheit() for temp in temps]

    for temp in kelvinTemps:
        if not temp.above_freezing():
            print(temp)

    for temp in celsiusTemps:
        if not temp.above_freezing():
            print(temp)

    for temp in fahrenTemps:
        if not temp.above_freezing():
            print(temp)
