from math import sqrt
a = input("Podaj liczbe nieujemna:")
a = float(a)
if a < 0:
    print("Prosze podac liczbe nieujemna")
else:
    print(sqrt(a))
