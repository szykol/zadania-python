# Zadanie 2.3

Napisz program, który tworzy obiekt klasy **Person**. Klasa posiada
atrybuty: **name**, **surname**, **age**. Program pozwala na uzupełnienie wartości atrybutów
danymi podanymi z klawiatury. Wiek musi być liczbą całkowitą w zakresie od 0 do
130, a imię i nazwisko muszą posiadać minimum 3 znaki - wykorzystaj w tym celu
właściwości. Klasa Person powinna definiować metodę **\__str__()**. Następnie, zaimplementuj dwie klasy **Student** i **Employee**, oparte na klasie Person. W klasie Student
dodaj atrybuty **field_of_study** i **student_book** - słownik, którego klucze to nazwy
przedmiotów, a wartości to oceny. W klasie Employee dodaj atrybut **job_title** i **skills** - lista kluczowych umiejętności. Zaimplementuj odpowiednie metody pozwalające na
uzupełnianie i wyświetlanie wartości atrybutów w obu klasach potomnych.