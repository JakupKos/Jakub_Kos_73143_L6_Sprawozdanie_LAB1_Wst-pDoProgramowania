#=====================================================
# zad. 6a
import random
dystans = random.randint(1,46545)

#dystans = float(input("Podaj pokonany dystans (km)"))
spalanie = float(input("Podaj średnie spalanie samochodu (l/100km)"))
cena_paliwa = float(input("Podaj cene paliwa (zł/l)"))

zużyte_paliwo = dystans * spalanie / 100
koszt_paliwa = zużyte_paliwo * cena_paliwa

print("Przewidywane zużycie paliwa to:", zużyte_paliwo, "litrów"
      "\nSzacowany koszt podrózy wynosi:", koszt_paliwa, "złotych",
      "\nPrzejeżdżając", dystans, "kilometrów")

"""
Przy pomocy funkcji random.randint() losowany jest przejechany dystans
"""

