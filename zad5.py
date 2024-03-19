import sys as system
import math
system.stdout.write('Wpisz liczbe calkowita:')
a = system.stdin.readline()
system.stdout.write('Wpisz druga liczbe calkowita:')
b = system.stdin.readline()
system.stdout.write('Wpisz trzecia liczbe calkowita:')
c = system.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
d = math.pow(a, b)
e = d+c
e = str(e)
system.stdout.write(e)


