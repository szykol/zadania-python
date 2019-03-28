def gen_calk():
    ''' Generuje dodatnie liczby calkowite zwiekszajac je o 1 '''
    l = 1
    while True:
        yield l
        l += 1

def kwadraty():
    ''' Generuje kwadraty dodatnich liczb calkowitych zwiekszanych o 1 '''

    for c in gen_calk():
        yield c ** 2

def select(gen, n):
    ''' Tworzy n-elementową listę wartości dowolnego obiektu iterowalnego 
        Wersja bez bezpośredniego używania iter() i next() '''

    import itertools
    return list(itertools.islice(gen(), n))

def select_it(gen, n):
    ''' Tworzy n-elementową listę wartości dowolnego obiektu iterowalnego '''
    it = iter(gen())

    l = []
    for _ in range(n):
        l.append(next(it))

    return l

def trojki():
    ''' Generuje trójki pitagorejskie '''
    c = 1
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    yield (a,b,c)
                    
        c += 1


print(select(trojki, 15))

