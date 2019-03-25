# Zadanie 2.2
W module **figure_module** zdefiniuj klasę **Figure**. Konstruktor klasy
Figure powinien definiować i inicjalizować (wartościami domyślnymi) dwa atrybuty
**colour** i **is_filled** (wartość True lub False). W klasie powinny być także zdefiniowane metody specjalne **\__str__()** oraz **\__repr__()**. Następnie zdefiniuj dwie klasy
**Circle** i **Rectangle** dziedziczące po klasie Figure. Konstruktor klasy Circle powinien wywoływać konstruktor klasy bazowej i definiować dodatkowy atrybut **radius** -
wykorzystaj właściwość, aby zabezpieczyć atrybut przed ustawieniem niepoprawnych
danych (wykorzystaj właściwości). W klasie powinny być zdefiniowane także właściwości zwracające wartość pola, obwodu i średnice - area, perimeter, diameter. Klasa Circle powinna też posiadać metody specjalne __str__() oraz __repr__() - tam
gdzie to uzasadnione wykorzystaj wywołanie metody klasy bazowej. Konstruktor klasy
Rectangle powinien wywoływać konstruktor klasy bazowej i definiować dodatkowe
atrybuty **width** i **height** - wykorzystaj właściwości, aby zarządzać tymi atrybutami.
Wyposaż tę klasę w odpowiednie właściwości i metody specjalne analogiczne jak w
klasie Circle (zamiast średnicy rozważ przekątną - diagonal). Przetestuj klasy Circle
i Rectangle. Uwaga: Metoda \__repr__() w klasach Circle i Rectangle powinna być
tylko dziedziczona po klasie bazowej i powinna działać dobrze dla wszystkich wspominanych klas (wykorzystaj specjalny atrybut instancji \__dict__ - słownik przechowujący
nazwy atrybutów powiązane z ich wartościami).
