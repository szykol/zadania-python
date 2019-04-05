# Zadanie 4.3

Zaprojektuj klasę **SortedList** - przechowująca listę elementów posortowanych w kolejności. Klasa powinna być oparta o abstrakcyjną klasę bazową
Sequence z modułu collections.abc Klasa powinna tworzyć posortowaną listę elementów w oparciu o opcjonalny klucz sortowania. Stworzona klas powinna mieć interfejs zbliżony do **wybudowanego typu list** - (bez metod insert(), reverse() oraz
sort()). Zamiast metody append() zastosuj metodę add() wstawiająca dany element
w odpowiednie miejsce - w tym celu wykorzystaj metodę chronioną **_find_index()**,
która zwraca odpowiednią pozycje indeksu (zastosuj algorytm wyszukiwania binarnego)).