napis = input('Podaj napis:')
napis_bez_spacji = napis.replace(' ', '')  # zeby sprawdzic czy zdanie jest palindromem - usuwamy spacje
k = 0
for i in range(len(napis_bez_spacji) // 2):
    if napis_bez_spacji[i] == napis_bez_spacji[-1 - i]:
        k += 1
if k == len(napis_bez_spacji) // 2:
    print('Napis jest palindromem')
else:
    print('Napis nie jest palindromem')
