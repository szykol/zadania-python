# Zadanie 2.4
Zdefiniuj klasę **Rectangle** z dwoma atrybutami: **length** i **height** -
długości boków. Klasa powinna posiada następujące metody:
- \__init__();
- area() - zwraca pole;
- \__str__();
- \__repr__()

Zdefiniuj klasę **Cuboid** dziedziczącą po klasie Rectangle i mającą dodatkowy atrybut
**width** oraz metody:
- \__init__() - wywołuje konstruktor klasy bazowej;
- area() - zwraca pole powierzchni prostopadłościanu (wykorzystaj odpowiednią
metodę klasy bazowej);
- volume() - metoda ma zwracać objętość prostopadłościanu (wykorzystaj
odpowiednią metodę klasy bazowej);
- \__str__();
- \__repr__()

Inicjalizacja atrybutów instancji klas powinna odbywać się poprzez wartości jej parametrów.
Napisz program, w której wczytasz dane z pliku tekstowego - dane czytane do końca pliku. W kolejnych wierszach dane: liczba 1 lub 2 (1-prostokąt, 2-prostopadłościan),
a następnie oddzielone spacjami, w przypadku prostokąta długość i wysokość zaś w
przypadku prostopadłościanu długość, wysokość i szerokość. Wypisz na ekranie monitora typ figury, parametry ją charakteryzujące i pole powierzchni, a dla prostopadłościanu także objętość. Zastosuj obsługę wyjątków. Zdefiniuj własną klasę **InvalidData**
dziedzicząca po Exception. Wykorzystaj tę klasę do obsługi sytuacji wyjątkowych:
ujemne lub zerowe długości boków/krawędzi. Obsłuż błędy IO i błąd złego typu danych.