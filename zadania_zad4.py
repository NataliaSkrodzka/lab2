n = input('Podaj liczbe naturalna:')
n = int(n)
k = 0
for i in range(2, n):
    if n % i == 0:
        k += 1
if n < 0:
    print('Podana liczba jest ujemna czyli nie jest naturalna')
else:
    if (n == 1) or (n == 0):
        k += 1

    if k > 0:
        print('Liczba nie jest liczba pierwsza')
    else:
        print('Liczba jest liczba pierwsza')
