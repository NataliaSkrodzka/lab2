zdanie = input('Wpisz zdanie:')
k = 1
for i in range(len(zdanie)):
    if zdanie[i] == ' ':
        k += 1
print(k)
