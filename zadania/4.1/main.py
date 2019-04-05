class Pupil:
    OCENY = set([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6])

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.marks = {}

    def set_marks(self):
        while True:
            przedmiot = input('Wprowadź nazwę przedmiotu: (q by wyjść): ')
            if not przedmiot:
                continue
            if przedmiot.lower() == 'q':
                break
            try:
                ocena = float(input('Wprowadz ocenę z zakresu [1;6]: '))
                if ocena not in Pupil.OCENY:
                    raise ValueError
            except ValueError:
                print('Wprowadź prawidłową liczbę!')
            else:
                self.marks[przedmiot] = ocena

    def print_marks(self):
        print('-' * 5, 'Oceny', '-' * 5)
        for k,v in self.marks.items():
            print(f'{k}: {v}')

        print('-' * 17)
    
    def mean(self):
        from functools import reduce
        if len(self.marks) == 0:
            return 0.0

        sum = reduce(lambda a,b: a + b, self.marks.values())
        return sum/len(self.marks)

    def __str__(self):
        return f'{self.name} {self.surname} | {self.mean()}'

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) >= 3:
            self.__name = name
        else:
            self.__name = 'name'
    
    @property
    def surname(self):
        return self.__surname
    
    @surname.setter
    def surname(self, surname):
        if len(surname) >= 3:
            self.__surname = surname
        else:
            self.__surname = 'surname'
    
class Student(Pupil):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.weights = {}

    def complete_weights(self):
        for key in self.marks:
            while True:
                try:
                    waga = float(input(f'Wprowadz wagę z zakresu (0;1] dla przedmiotu {key}: '))
                    if waga <= 0 and waga > 1:
                        raise ValueError
                except ValueError:
                    print('Wprowadź prawidłową liczbę!')
                else:
                    self.weights[key] = waga
                    break

    def mean(self):
        if len(self.marks) == 0:
            return 0.0
        sum_marks = 0
        sum_weights = 0

        for key, val in self.marks.items():
            weight = self.weights[key]
            sum_marks += val * weight
            sum_weights += weight

        return sum_marks / sum_weights

    def __str__(self):
        return super().__str__()

if __name__ == "__main__":
    p = Pupil('Antonio', 'Banderas')
    p.set_marks()
    p.print_marks()
    print(p)

    s = Student('Drugi', 'Uczen')
    s.set_marks()
    s.complete_weights()
    s.print_marks()
    print(s)