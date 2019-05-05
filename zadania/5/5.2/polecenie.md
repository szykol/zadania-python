# Zadanie 5.2
 
Zmodyfikuj plik **platform_game_2_move.py** tworząc nowy plik o
nazwie **platform_game_3_platforms.py**. Modyfikacja powinna polegać na dodaniu
trzech klas.
-   Platform oparta o klasę wbudowaną **pygame.sprite.Sprite** i posiadającą następujące metody:
    -   metoda **\_\_init__()** o parametrach: **colour, width, height, rect_x, rect_y**; konstruktor powinien incjalizować następujące atrybuty **width** i **height** wartościami odpowidenich parametrów oraz tworzyć atrybut **rect** inicjalizując go instancją pygame.Surface([width, height]); użyj metody **fill** aby wypełnić prostokąt odpowiednim kolorem oraz zmodyfikuj wartość atrybutów rect.x i rect.y wartościami odpowiednich parametrów;
    -   metoda **draw**() analogiczna jak w klasie Player.
-   ogólna klasa reprezentująca planszę gry Level, która posiada następujące metody:
    -    metoda **\_\_init__()** o parametrze będącym instancją klasy Player; konstruktor powinien tworzyć dwa atrybuty: player incijalizowany parametrem oraz set_of_platforms - incijalizowany pustym zbiorem, który będzie zawierał obiekty klasy Platform;
    -    metoda **update**(), która wywołuje metodę update() każdego z obiektów z kolekcji set_of_platforms;
    -    metoda **draw**(), która wywołuje metodę draw() każdego obiektu ze zbioru set_of_platforms.
-   Klasa **Level_1** oparta o klasę Level i zawierające metodę konstruktora; konstruktor powinien wywoływać metodę klasy bazowej oraz tworzyć i dodawać do zbioru **set_of_platforms** kilka obiektów klasy Platform (uwaga: wysokość platform
powinna być równa 70, a jej szerokość powinna być wielokrotnością tej liczby).
Utwórz obiekt klasy Level_1 i powiąż go wzajemnie z obiektem klasy Player. W pętli
gry wywołaj odpowiednie metody instancji klasy Level_1.
