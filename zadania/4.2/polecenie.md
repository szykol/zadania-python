# Zadanie 4.2

Opracuj abstrakcyjną klasę bazową o nazwie **Temperature**, która
przechowuje pojedynczą wartość temperatury. Klasa powinna mieć następujący nagłówek metody **\_\_init__**() (rzeczywiście zaimplementowana metoda abstrakcyjna):

```
def __init__ (self, temperature)
```

Oprócz tego abstrakcyjna klasa Temperature powinna zawierać następujące metody:
- **\_\_str__**() - powinien zwrócić ciąg postaci "75 stopni w skali Celsjusz" (metoda
konkretna);
- **\_\_repr__**() - powinien zwrócić ciąg postaci "ClassName(temperature)" (metoda
konkretna);
- **above_freezing**() - zwraca True jeśli temperatura powyżej punktu zamarzania
(metoda konkretna);
- **convert_to_Fahrenheit**() - zwraca nowy obiekt temperatury przekształcony na
stopnie Fahrenheita (metoda abstrakcyjna);
- **convert_to_Celsius**() - zwraca nowy obiekt temperatury przekształcony na
stopnie Celsjusza (metoda abstrakcyjna);
- **convert_to_Kelvin**() - zwraca nowy obiekt temperatury przekształcony na
stopnie Kelvina (metoda abstrakcyjna);
- właściwości **temperature** typu setter i getter (abstrakcyjne właściwości).

Opracuj podklasy **Fahrenheit**, **Celsius** i **Kelvin** i odpowiednio wdróż każdą z metody
abstrakcyjnej klasy Temperature. (Należy pamiętać, że gdy stosowana jest bezsensowna metoda konwersji, np. wywołanie metody, temp1.convert_to_Fahrenheit(), gdzie
temp1 jest instancją klasy Fahrenheit, powinno zwracać ten sam obiekt temperatury.

Sprawdź poprawność swoich klas w następujący sposób:
- stwórz listę zawierającą 12 instancji klas (każdej po cztery egzemplarze) Kelvin,
Celsius i Fahrenheit;
- wydrukuj obiekty listy, a dla temperatur które są powyżej temperatury zamarzania wody dodaj adnotację "powyżej zera";
- utwórz trzy listy zawierające każdą temperaturę z pierwotnej listy przekształconą
do wspólnej skali temperatur (Fahrenheita, Celsjusza, lub Kelvina);
- z każdej z utworzonych list wydrukuj tylko te, które są poniżej temperatury zamarzania wody.
Oto potrzebne przeliczniki:

```
Celsjusz = 0.556 * ( Fahrenheit - 32.0)
Kelwin = Celsjusz + 273.16
```