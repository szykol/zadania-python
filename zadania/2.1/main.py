# -*- coding: utf-8 -*-

from notes import Note, Notebook
import sys

class Menu:
    def __init__(self):
        self.options = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

        self.notebook = Notebook()

    def show_notes(self):
        """ Pokaz notatki """
        
        for note in self.notebook.notes:
            print(note)

    def search_notes(self):
        """ Wyszukaj notatki z daną zawartością """
        found = self.notebook.search()
        if found:
            for note in found:
                print(note)


    def add_note(self):
        """ Dodaj notatkę """
        self.notebook.new_note()

    def modify_note(self):
        """ Edytuj notatkę """

        print('1) Edytuj tytuł')
        print('2) Edytuj treść')
        option = input('> Wybirz opcje: ')

        if option == '1':
            self.notebook.modify_tag()
        elif option == '2':
            self.notebook.modify_text()
        else:
            print('Wprowadz poprawne dane')


    def quit(self):
        """ Wyjście """
        sys.exit(0)

    def show_menu(self):
        for key, val in self.options.items():
            print('{key}) {val}'.format(val=val.__doc__, key=key))

    def run(self):
        while True:
            self.show_menu()
            option = input('> Wybierz opcję: ')

            if option in self.options:
                self.options[option]()
            else:
                print('Wybierz istniejącą opcję!')
        
if __name__ == "__main__":
    menu = Menu()
    menu.run()