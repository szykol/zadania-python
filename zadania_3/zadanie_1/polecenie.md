# Zadanie 3.1

Napisz program, który symuluje prosty system uwierzytelniania i
autoryzacji. W module authorization_system utwórz klasy:
- **User** - Przechowuje nazwę użytkownika i zaszyfrowane hasło. Klasa powinna zawierać metody:
    - **\_\_init__()** - tworzy i incjializuje atrybutu: username - nazwa użytkownika
podana podczas konkretyzacji obiektu; password - hasło (złożone z nazwy
użytkownika i hasła) podane podczas konkretyzacji obiektu, ale zaszyfrowane przez _encrypt_password(); is_logged - o początkowej wartości False;
    - **_encrypt_password()** - metoda zmieniająca hasło (podane jako argument
metody) i nazwę użytkownika na zaszyfrowaną wersję, którą zwraca (wykorzytaj moduł hashlib i np. funkcję skrótu SHA-256);
    - **check_password()** - metoda sprawdzająca hasło (podane jako argument metody) z hasłem przechowywanym w atrybucie i zwracająca True lub False.
- prostą klasę wyjątku **AuthenticException** z parometrowym konstruktorem, który tworzy i incjalizuje dwa atrybuty **username** i **user** - o wartości domniemanej
None.
- prostą hierarichę klas wyjątków o pustych ciałach (zob poniższy diagram UML)

![diagram](./diagram.png)

- klasę **Authenticator** - klasa kontrolująca użytkowników. Klasa powinna zawierać metody:
    - **\_\_init__()** - tworzy i incjializuje pustym słownikiem atrybut users;
    - metoda **add_user**, która umożliwia dodanie użytkownika (o podanej nazwie i haśle) do słownika user pod warunkiem, że w słowniku nie ma takiego użytkownika (w przeciwnym wypadku następuje podsinienie wyjątku
**UsernameAlreadyExists**) oraz jego hasło ma więcej niż 7 znaków (w przeciwnym wypadku następuje podsinienie wyjątku **PasswordTooShort**);
    - metoda **login**, która służy do logowania (gdy użytkownik jest zalogowany
jago atrybut is_logged przyjmuje wartość True), metoda podnosi wyjątek
**IncorrectUsername**, gdy taki użytkownik nie ma konta (nie ma go w słowniku users) lub wyjątek **IncorrectPassword**, gdy hasło użytkownika jest
niepoprawne - gdy logowanie się powiedzie metoda powinna też zwrócić
wartość True;
    - metoda **is_logged_in** - zwraca odpowiednio True lub False gdy dany użytkownik jest lub nie jest zalogowany;
- klasę Authorizor, która mapuje uprawnienia dla użytkowników. Klasa powinna
zawierać metody:
    - **\_\_init__()** tworzy i incjializuje pustym słownikiem atrybut permissions
oraz atrybut authenticator inicjalizowany parametrem konstruktora;
    - metoda **add_permission**, która pozwala dodać do słownika nowe uprawnienie jako klucz z wartością będącą pustym zbiorem, jeżeli uprawnienie już
istnieje metoda podnosi wyjątek **PermissionError**
    - metoda **permit_user**, która umożliwia przypisanie danemu użytkownikowi podanemu jako argument metody odpowiedniego uprawnienia (drugi
argument metody). Metoda powinna podnosić w odpowiednich miejscach
wyjątki **PermissionError** oraz **IncorrectUsername**.
    - metoda **check_permission**, która pozwala sprawdzić czy podany użytkownik posiada wskazane uprawnianie. Metoda powinna podnosić odpowiednie wyjątki: **NotLoggedError** - gdy użytkownik nie jest zalogowany, **PermissionError** - gdy nie ma takiego uprawnienia, **NotPermittedError** - gdy użytkownik nie ma podanego uprawnienia.
Moduł zakończ stworzeniem instancji klasy **Authenticator** oraz **Authorizor** (argumentem konstruktora tej drugiej instancji jest oczywiście pierwszy obiekt).
W głównym programie utwórz odpowiednie instancje obiektów reprezentacyjnych
użytkowników i nadaj im uprawnienia (np. testowania i/lub zmieniania programów).

Stwórz klasę **Editor**, która zawiera podstawowy interfejs menu pozwalający niektórym
użytkownikom zmienić lub testować program. Wspomniana klasa powinna zawierać
metody:
- **\_\_init__()** - tworzy dwa atrybutu: username wartości None oraz options o wartosści self.options = {"a": self.login, "b": self.test, "c": self.change, "d": self.quit}.
- **login()** - metoda pobierająca od użytkownika nazwę i hasło oraz wywołująca
odpowiednią metodę login() stworzonej instancji klasy Authenticator wraz z
obsługą wyjątków;
- **is_permitted()** - metoda sprawdzająca czy użytkownik jest zalogowany i ma
odpowiednie uprawnienia (wywołuje metodę check_permission i obsługuje odpowiednie wyjątki);
- **test()** - metoda imitująca testowanie hipotetycznego programu (korzysta z metody is_permitted());
- **change()** - metoda imitująca zmienianie hipotetycznego programu (korzysta z
metody **is_permitted()**);
- **quit()** - metoda kończąca działanie głównego programu;
- **run()**, która zapewnia pobranie od użytkownika odpowiedniego klucza i odczytanie (wraz z wywołaniem) odwadniającej mu wartości słownika options.
Główny program powinien tworzyć instancje klasy **Editor** i wywoływać metodę **run()**.