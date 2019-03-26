class FibIt:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        next = self.a + self.b

        if next > self.n:
            raise StopIteration
        
        self.a = self.b
        self.b = next
        return next

def FibGen(n=None):
    a,b = 0,1
    next = a + b
    infinite = n is None
    while infinite or next <= n: 
        yield next
        next = a + b
        a, b = b, next

class FibSeq:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        n = 0
        val = None
        it = iter(FibGen())
        while n < self.start:
            next(it)
            n+=1

        while n < self.end:
            yield next(it)
            n+=1

        return 


with open('liczby.txt', 'w') as f:
    first = True
    for i in FibSeq(100000, 100020):
        f.write(f'{i}\n')
        if first:
            print(f'Ilosc cyfr F(100000): {len(str(i))}')
            first = False


