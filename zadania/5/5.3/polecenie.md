# Zadanie 5.3

Zmodyfikuj plik **platform_game_3_platforms.py** tworząc plik o nazwie **platform_game_4_jump.py**. Modyfikacja powinna dotyczyć klasy **Player**:
- utwórz metodę **_gravitation**, której wywołanie spowoduje zwiększenie wartość
atrybutu **movement_y** do 1 gdy był on zerem lub zwiększenie o np. 0.35; metoda
ta powinna być wywoływana w przez metodę **update()**;
- dodaj metodę **jump()**, która ustawi wartość atrybutu **movement_y** np. na −12 i wywołaj ją w metodzie **get_event()** w odpowiedzi na wciśnięcie jakiegoś klawisza;
- w metodzie **update()** dodaj kod, który modyfikuje położenie gracza w pionie
oraz kod który wykrywa kolizję z platformami (w czterech kierunkach) - wykorzystaj funkcję **pygame.sprite.spritecollide()** np. gdy gracz uderzy w obiekt
platformy swoją prawą stroną to wartość atrybutu gracza **rect.right** powinna
być ustawiona na wartość atrybutu platformy **rect.left** (z którą nastąpiła kolizja) - analogicznie należy postąpić w przypadku kolizji w pozostałych kierunkach ruchu; skorzystaj z grafik **gm.FALL_L**, **gm.FALL_R**, **gm.JUMP_L** oraz **gm.JUMP_L** aby
zmienić wygląd obiektu gracza w czasie skoku i spadania.