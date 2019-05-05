# Zadanie 5.4

Zmodyfikuj plik **platform_game_4_jump.py** tworząc plik o nazwie
**platform_game_5_platform_scroller**. Modyfikacja kodu powinna dotyczyć dwóch
klas: **Platform** oraz **Level**. W pierwszej klasie zmodyfikuj metodę **draw()** tak aby wypełniać platformę odpowiednią grafiką z listy będącej jej parametrem (lista czetoroelmentowa zob. dalej). Wywołując tę metodę w klasie Level przekaż jej listę grafik
**gm.GRASS_LIST**.
W konstruktorze klasy **Level** dodaj atrybut **world_shift** o wartości początkowej
równej zero. Następnie, dodaj parometrową metodę **_shift_world()**, która zwiększy
wartość atrybutu world_shift o wartość parametru tej metody, a także "przesunie"
wszystkie obiekty planszy o wartość tego parametru (na razie są to tylko obiekty ze
zbioru **set_of_platforms**). W metodzie **update()** dodaj dwa fragmenty kodu źródłowego. Pierwszy fragment powinien sprawdzać czy np. wartość **player.rect.right** jest
większe od 500, obliczać różnicę między player.rect.right oraz 500, wywoływać z
wartością tej różnicy (ze znakiem przeciwnym) metodę **_shift_world()** oraz ustawić
wartość atrybutu player.rect.right na 500. Drugi fragment kodu powinien działać
analogicznie, gdy np. wartość atrybutu **self.player.rect.left** będzie mniejsza od
150.