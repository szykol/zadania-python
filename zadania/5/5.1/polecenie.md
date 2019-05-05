# Zadanie 5.1
Zmodyfikuj plik platform_game_1_player.py tworząc nowy plik o
nazwie **platform_game_2_move.py**. Modyfikacja powinna opierać się m .in na dodaniu
do klasy Player następujących metod:
- metoda **turn_right()** - modyfikuje odpowiednio atrybut **movement_x** (wartość
dodatnia np. 6) oraz atrybut **direction_of_movement**;
- metoda **turn_left()** - zmienia atrybut **movement_x** (wartość taka sama jak w metodzie turn_right ale o ujemnym znaku) oraz atrybut **direction_of_movement**;
- metoda **stop()** - ustawia wartość atrybutu **movement_x** na zero;
- metoda **_move()**, która przyjmuje jako parametr dwuelementową listę grafik (np.
image_list) i w zależności od wartości atrybutu **count** (który powinien przy
każdym wywołaniu tej metody wzrastać o 1, ale cyklicznie w zakresie od 0 do 8),
powinien modyfikować wartość atrybuty image tj. dla wartości count od 0 do 4
atrybut image powinien mieć wartość pierwszej grafiki z listy, a w przeciwnym
wypadku drugiej;
- metoda **update()**, która modyfikuje położenie gracza (np. atrybut **rect.x**) o wartość atrybutu **movement_x** oraz wywołuje metodę **_move()** z parametrem odpowiednio **gm.IMAGES_R** lub **gm.IMAGES_L** w zależności o wartości movement_x;
- metoda get_event, która jako parametr przyjmuje zdarzenie i w zależności od
wartości tego parametru (wciśnięcie/puszczenie odpowiedniego klawisza) wywołuje metodę **turn_right()**, **turn_left()** lub **stop()**.
W pętli zdarzeń wywołaj metodę get_event, a w pętli gry metodę **update()** obiektu
***player***
