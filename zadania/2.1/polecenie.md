# Zadanie 2.1
Napisz program, który będzie symulował bardzo prosty notatnik.
Utwórz plik modułu, który zawiera klasy: **Note** i **Notebook**. Konstruktor pierwszej klasy powinien tworzyć i inicjalizować atrybuty **text** i **tag** (dane przekazane przez parametry konstruktora) atrybut **date** (automatyczna data tworzenia notatki) oraz atrybut
**ID** (automatyczny numer notatki w danym notatniku - inicjalizowany przez odpowiedni atrybut klasy zliczający liczbę już utworzonych instancji klasy). Klasa Note powinna posiadać także metodę **match**, która zwraca True lub False jeżeli text lub tag zawiera przekazany do tej metody ciąg tekstowy. Konstruktor klasy Notebook powinien
tworzyć i inicjalizować pustą listą - atrybut **notes**. Klasa Notebook powinna posiadać
następujące metody:
- **new_note()** - pozwala na dodanie obiektu klasy Note do notatnika (listy notes);
- **modify_text()** - pozwalająca na zmianę tekstu notatki o podanym ID;
- **modify_tag()** - pozwalająca na zmianę tekstu etykiety notatki o podanym ID;
- **search()** - zwraca listę notatek zawierających szukaną frazę (w tekście lub etykiecie notatki).

Główny program powinien importować klasy, które są przedstawione wyżej i definiować nową klasę **Menu**. Konstruktor klasy Menu powinien tworzyć następujące atrybuty:
**notebook** - inicjalizowany obiektem klasy Notebook, **options** - inicjalizowany słownikiem: {"1": self.show_notes, "2": self.search_notes, "3": self.add_note,
"4": self.modify_note, "5": self.quit}. We wspominanej klasie zdefiniuj metody: **show_menu()** - wyświetlająca menu notatnika; **run()** - zapewniająca pobranie odpowiedniego klucza i odczytanie odwadniającej mu wartości słownika options; metody
odpowiadające wartościom słownika options tzn. show_notes(), search_notes() itd.
(łatwo wywnioskować jak mają działać te metody).
### Uwaga:
 Metoda search_notes()
powinna wyświetlać znalezioną listę notatek (zawierających szukaną frazę) za pomocą
wywołania metody show_notes() (jak?)