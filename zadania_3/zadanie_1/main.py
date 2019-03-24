from authorization_system import *
import sys

class Editor:
    def __init__(self):
        self.username = None
        self.options = {
            'a': self.login,
            'b': self.test,
            'c': self.change,
            'd': self.quit
        }

    def login(self):
        """ Login """
        login = input('Podaj login')
        password = input('Podaj haslo')

        try:
            authenticator.add_user(login, password)
        except UsernameAlreadyExists:
            try:
                authenticator.login(login, password)
            except IncorrectUsername:
                print('Niepoprawna nazwa uzytkownika')
            except IncorrectPassword:
                print('Niepoprawne haslo')
            else:
                self.username = login
        except PasswordTooShort:
            print('Podane haslo nie jest dluzsze niz 7 znakow')

        return True

    def is_permitted(self, permission):
        """ Check permission """
        try:
            authorizor.check_permission(self.username, permission)
        except NotLoggedError:
            print('Uzytkownik nie jest zalogowany')
        except PermissionError:
            print('Nie ma takiego uprawnienia')
        except NotPermittedError:
            print('Uzytkownik nie ma uprawnienia')
        else:
            print('Uzytkownik ma uprawnienie')
    
    def test(self):
        """ Test """
        self.is_permitted('Testowanie')

    def change(self):
        """ Change """
        self.is_permitted('Edycja')

    def quit(self):
        """ Quit """
        sys.exit(0)

    def run(self):
        while True:
            for key, val in self.options.items():
                print('{key}) {val}'.format(val=val.__doc__, key=key))

            option = input('> Wybierz opcję: ')

            if option in self.options:
                self.options[option]()
            else:
                print('Wybierz istniejącą opcję!')

if __name__ == "__main__":
    authenticator.add_user('Pierwszy', 'Haslo777')
    authenticator.add_user('Drugi', 'Drugie777')

    authorizor.add_permission('Edycja')
    authorizor.add_permission('Testowanie')

    authorizor.permit_user('Pierwszy', 'Edycja')
    authorizor.permit_user('Drugi', 'Edycja')
    authorizor.permit_user('Drugi', 'Testowanie')

    try:
        print(authorizor.check_permission('Pierwszy', 'Edycja'))
        print(authorizor.check_permission('Pierwszy', 'Testowanie'))
    except AuthenticException as e:
        print('Problem z autoryzacja')


    Editor().run()
    



