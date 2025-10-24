#=====================================================
# zad. 1A
działania = [
    1 + 2,
    1 + 4.5,
    3 / 2,
    4 / 2,
    3 // 2,
    -3 // 2,
    11 % 2,
    2 ** 10,
    8 ** (1/3) ]

for x in działania:
    print(x, type(x))
"""
Operatory:
+ dodawanie
/ dzielenie
// dzielenie całkowite
% dzielenie modulo, reszta z dzielenia 
** potęgowanie
"""
#=====================================================
# zad. 1B
print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))
"""
int(3.0) zamienia liczbę zmiennoprzecinkową na liczbę całkowitą
float(3) zamienia liczbę całkowitą na liczbę zmiennoprzecinkową
float("3") zamienia napis "3" na liczbę zmiennoprzecinkową
str(12.4)  tworzy ciąg danych, łańcuch znaków
bool(0) logiczny typ danych prawda/fałsz
"""