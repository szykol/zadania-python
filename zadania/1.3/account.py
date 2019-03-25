class Account:
    def __init__(self, val):
        self._balance = val

    def pay(self, val):
        self._balance += val

    def take(self, val):
        if self._balance - val >= 0:
            self._balance -= val
        else:
            print('Brak środków')
    
    def show_balance(self):
        return self._balance
    
    def __str__(self):
        return f'Oto wartość twojego konta bankowego: {self._balance}'

