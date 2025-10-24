#=====================================================
# zad. 6
dystans = float(input("Podaj pokonany dystans (km)"))
spalanie = float(input("Podaj średnie spalanie samochodu (l/100km)"))

zużyte_paliwo = dystans * spalanie / 100
koszt_paliwa = zużyte_paliwo * 6.5

print("Przewidywane zużycie paliwa to:", zużyte_paliwo, "litrów" 
      "\nSzacowany koszt podrózy wynosi:", koszt_paliwa, "złotych")

"""
Przy pomocy zapisania zmiennych w postaci float można nimi wykonywać działania matematyczne,
Przy użyciu "\n" w funkcji print() można zapisać dwie linijki tekstu przy pomocy jednej funkcji print zamiast dwóch
"""