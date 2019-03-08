# -*- coding: utf-8 -*-
import datetime

class Note:
    """ Class representing a single note with it's tag """
    newest_ID = 0

    def __init__(self, text, tag):
        self.text, self.tag = text, tag
        self.ID = Note.newest_ID
        Note.newest_ID += 1
        self.date = datetime.datetime.now()

    def __str__(self):
        return 'Tytul: {tag}\nTreść: {text}'.format(tag=self.tag, text=self.text)

    def match(self, string):
        return string in self.text or string in self.tag

    
class Notebook:
    """ Class representing notes put together as a single notebook """
    
    def __init__(self):
        self.notes = []

    def new_note(self):
        tag = input('Wprowadź tytuł notatki: ')
        text = input('Wprowadź zawartość notatki: ')

        if tag and text:
            self.notes.append(Note(text, tag))
        else:
            print('Wprowadź tytuł i zawartość notatki: ')

    def modify_text(self):
        note = self.get_note()
        if note:
            text = input('Wprowadź zawartość notatki')
            if text:
                note.text = text
            else:
                print('Wprowadź zawartość notatki: ')
    
    def modify_tag(self):
        note = self.get_note()
        if note:
            tag = input('Wprowadź tytuł notatki')
            if tag:
                note.tag = tag
            else:
                print('Wprowadź tytuł notatki: ')

    def get_note(self):
        ID = input('Podaj ID notatki: ')
        try:
            ID = int(ID)
        except ValueError:
            print('Wprowadź liczbę całkowitą')
        else:
            for note in self.notes:
                if note.ID == ID:
                    return note
        
        print('Nie znaleziono notatki z tym ID')
            
    def search(self):
        string = input('Wprowadź szukaną frazę: ')
        return list(filter(lambda note: note.match(string), self.notes))

