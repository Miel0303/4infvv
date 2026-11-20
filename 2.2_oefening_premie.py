uren = float(input("Hoeveel uur heb je deze maand gewerkt?: "))
uurloon = 8.5
loon = uren * uurloon

if uren > 20:
    loon = loon + 25
    print("Proficiat, je krijgt een premie van 25 euro!")

print("Je verdient deze maand " + str(loon) + " euro.")

