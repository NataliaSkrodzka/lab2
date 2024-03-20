for i in range(2, 1000):
    suma = 0
    for j in range(1, i):
        if i % j == 0:
            suma += j
    if suma == i:
        print('liczba', i, 'jest doskonala')
