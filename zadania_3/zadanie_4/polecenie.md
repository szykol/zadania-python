# Zadanie 3.4
Napisz generator **gen_time**, który produkuje kolejne sekwencję czasu
w postaci krotki (godziny, minuty, sekundy). Generator powinien przyjmować w
postaci krotek czasu czas startowy, czas końcowy i krok czasu. Zamiast zwykłych krotek
możesz skorzystać z krotek nazwanych. Przykładowe działanie:
```
>>> for time in gen_time ((8, 10, 00), (10, 50, 15), (0, 15, 12) ):
    print(time)
    
(8, 10, 0)
(8, 25, 12)
(8, 40, 24)
(8, 55, 36)
(9, 10, 48)
(9, 26, 0)
(9, 41, 12)
(9, 56, 24)
(10, 11, 36)
(10, 26, 48)
(10, 42, 0)
>>>
```