#=====================================================
# zad. 6a_f-string
import random
dystans = random.randint(1,46545)

#dystans = float(input("Podaj pokonany dystans (km)"))
spalanie = float(input("Podaj średnie spalanie samochodu (l/100km)"))
cena_paliwa = float(input("Podaj cene paliwa (zł/l)"))

zużyte_paliwo = dystans * spalanie / 100
koszt_paliwa = zużyte_paliwo * cena_paliwa

print(f"Przewidywane zużycie paliwa to: {zużyte_paliwo} litrów"
      f"\nSzacowany koszt podrózy wynosi: {koszt_paliwa} złotych",
      f"\nPrzejeżdżając {dystans} kilometrów")

"""
Korzystając z f-string można wstawić wartości zmiennych bezpośrednio do tekstu
"""
