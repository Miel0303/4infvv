getal1 = float(input("geef getal 1:") )
bewerking = input("Welke bewerking? (+, -, *, /, **): ")
getal2 = float(input("Geef getal 2: "))

if bewerking == "+" :
    resultaat = getal1 + getal2
    print(str(getal1) + "+" + str(getal2) + "=" + str(round(resultaat,2))) 
if bewerking == "-" :
    resultaat = getal1 - getal2
    print(str(getal1) + "-" + str(getal2) + "=" + str(round(resultaat,2)))
if bewerking == "/" :
    resultaat = getal1 / getal2
    print(str(getal1) + "/" + str(getal2) + "=" + str(round(resultaat,2))) 
if bewerking == "*" :
    resultaat = getal1 * getal2
    print(str(getal1) + "*" + str(getal2) + "=" + str(round(resultaat,2)))
if bewerking == "**" :
    resultaat = getal1 ** getal2
    print(str(getal1) + "**" + str(getal2) + "=" + str(round(resultaat,2)))


