class Person:
    def __init__(self):
        self.set_name()
        self.set_surname()
        self.set_age()
        
    def __str__(self):
        return f'Imie: {self.name} Nazwisko: {self.surname} Wiek: {self.age}'
    
    def set_name(self):
        name = input('Podaj imie: ')
        self.name = name

    def set_surname(self):
        surname = input('Podaj nazwisko: ')
        self.surname = surname
    
    def set_age(self):
        age = int(input('Podaj wiek: '))
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) >= 3:
            self.__name = name
        else:
            self.__name = 'default name'

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if len(surname) >= 3:
            self.__surname = surname
        else:
            self.__surname = 'default name'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 <= age <= 130:
            self.__age = age
        else:
            self.__age = 0

class Student(Person):
    def __init__(self):
        super().__init__()
        self.set_field_of_study()
        self.student_book = {}
        self.set_student_book()

    def __str__(self):
        return super().__str__() + f'\nKierunek: {self.field_of_study} | {self.student_book}'

    def set_student_book(self):
        while True:
            name = input('Podaj nazwę przedmiotu (q by wyjść): ')
            if name == 'q': break
            ocena = float(input('Podaj ocenę'))
            if name and 0 < ocena <= 6:
                self.student_book[name] = ocena

    def set_field_of_study(self):
        fos = input('Wprowadz kierunek studiów: ')
        if fos: self.field_of_study = fos

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.set_job_title()
        self.skills = []
        self.set_skills()

    def __str__(self):
        return super().__str__() + f'\nPraca: {self.job_title} | Umiejętności: {self.skills}'

    def set_job_title(self):
        title = input('Wprowadz nazwę pracy: ')
        if title:
            self.job_title = title
        else:
            self.job_title = 'default job title'

    def set_skills(self):
        while True:
            skill = input('Wprowadź umiejętność (q by wyjść): ')
            if skill == 'q': break
            self.skills.append(skill)

if __name__ == "__main__":
    e = Employee()
    print(e)