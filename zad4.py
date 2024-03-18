napis = input("Podaj napis:")
print(napis)
k = 0
for x in range(len(napis)):
    if napis[x] == 'a' or napis[x] == 'A':
        k += 1

print(k)
