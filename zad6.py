a = input("Podaj pierwsza liczbe:")
b = input("Podaj druga liczbe:")
c = input("Podaj trzecia liczbe:")
a = int(a)
b = int(b)
c = int(c)
if a >= b:
    if a >= c:
        print(a, "jest najwieksza")
    else:
        print(c, "jest najwieksza")
else:
    if b >= c:
        print(b, "jest najwieksza")
    else:
        print(c, "jest najwieksza")





