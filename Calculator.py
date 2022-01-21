a = float(input("Wpisz pierwszą liczbę: "))
b = float(input("Wpisz drugą liczbę: "))

dzialanie = str(input(""" 
dodawanie: +
odejmowanie: -
dzielenie: / 
mnożenie: *

Wybierz działanie: """))

if dzialanie == "+":
    print("\nWynik dodawania: ", a + b)
elif dzialanie == "-":
    print("\nWynik odejmowania: ", a - b)
elif dzialanie == "/":
    if b == 0:
        quit("Nie można dzielić przez 0!")
    print("\nWynik dzielenia: ", a / b)
elif dzialanie == "*":
    print("\nWynik mnożenia: ", a * b)
else:
    quit("Podałeś niepoprawny znak działania.")