resultaat = float(input("Hoeveel punten heb je gehaald?: "))
totaal = float(input("Op hoeveel punten stond de toets?: "))
procent = totaal / resultaat * 100
print("Je hebt " + procent + "%")
if procent >= 50:
    print("Proficiat, je bent geslaagd!")
if procent < 50:
    print ("Jammer, je bent niet geslaagd.")
