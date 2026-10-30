getal1 = float(input("Hoeveel uur heb je deze maand gewerkt?: "))
getal2 = 8.5
som = getal1 * getal2

if getal1 > 20 :
    resultaat = som + 25
    print("Proficiat, je krijgt een premie van 25 euro!")
    print("Je verdient deze maand" + som + "euro")
if getal1 <= 20 :
    resultaat = som
    print("Je verdient deze maand" + som + "euro.")
