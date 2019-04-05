# Zadanie 4.1

Zdefiniuj dwie klasy:

### Klasa Pupil zawierająca:
- konstruktor z dwoma parametrami **imię** i **nazwisko** - wykorzystaj właściwości
do kontroli poprawności atrybutów name i surname - ciągi tekstowe składające
się z co najmniej **3 liter**; konstruktor powinien także definiować atrybut **marks** -
słownik przechowujący oceny (kluczem nazwa przedmiotu a wartością ocena -
liczba rzeczywiste ze zbioru {1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6});
- **complete_marks**() - dodaje przedmioty oraz oceny do słownika i kontroluje ich
poprawność (słownik uzupełnia użytkownik);
- **print_marks**() - wyświetla przedmioty i oceny;
- **metoda mean**() - zwraca średnią z ocen,
- **\_\_str__**() - zwraca napis składający się z imienia i nazwiska oraz średniej ocen.

### Klasa Student dziedzicząca z klasy Pupil:
- zawiera konstruktor z parametrami wywołujący konstruktor klasy nadrzędnej z
dodatkowym atrybutem **weights** - słownik z takimi samymi kluczami jak marks
i wartościami oznaczającymi wagi (liczby rzeczywiste z przedziału (0, 1])
- **complete_weights**() - przypisuje wagę dla każdego przedmiotu i kontroluje jej
poprawność (słownik uzupełnia użytkownik);
- zawiera przesłoniętą metodę **mean**(), która ma liczyć średnią ważoną.
- zawiera metodę **\_\_str__**() - zwraca napis składający się z imienia i nazwiska oraz
średniej ocen - wykorzystaj metodę klasy bazowej.

Następnie utwórz jeden obiekt klasy Pupil i jeden klasy Student z takimi samymi ocenami i sprawdź, jak są liczone ich średnie.