#=====================================================
# zad. 6
dystans = float(input("Podaj pokonany dystans (km)"))
spalanie = float(input("Podaj średnie spalanie samochodu (l/100km)"))

zużyte_paliwo = dystans * spalanie / 100
koszt_paliwa = zużyte_paliwo * 6.5

print(f"Przewidywane zużycie paliwa to: {zużyte_paliwo} litrów" 
      f"\nSzacowany koszt podrózy wynosi: {koszt_paliwa} złotych")

"""
Korzystając z f-string można wstawić wartości zmiennych bezpośrednio do tekstu
"""