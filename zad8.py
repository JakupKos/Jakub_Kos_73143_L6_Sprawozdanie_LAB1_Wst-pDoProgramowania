#=====================================================
# zad. 8
import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4 * a * c

if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Równanie ma dwa rozwiązania: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Równanie ma jedno rozwiązanie: x = {x}")
else:
    print("Równanie nie ma rozwiązań")