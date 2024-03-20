lista = ['Ala', 'ma', 2, 'koty', 'i', 1.5, 'psa', 'psa']
slownik = {}
slownik2 = {}
for i in range(len(lista)):
    slownik[lista[i]] = slownik.get(lista[i], 0) + 1
print(slownik)
for i in slownik:
    if isinstance(i, (int, float)):
        slownik2[i] = slownik.get(i)
print(slownik2)
