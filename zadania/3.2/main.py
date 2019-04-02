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

def select(iterowalny, n):
    ''' Tworzy n-elementową listę wartości dowolnego obiektu iterowalnego '''
    it = iter(iterowalny)

    l = []
    for _ in range(n):
        try:
            l.append(next(it))
        except StopIteration:
            break

    return l

trojki = ((a, b, c) for c in gen_calk() for b in range(1, c) for a in range(1, b) if a**2 + b**2 == c**2)

print(select(trojki, 15))

