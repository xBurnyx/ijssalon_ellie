from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs , korting):
        berekening = prijs - (prijs * korting)
        uitvoer1 = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {berekening} euro."
        return uitvoer1

def inkomsten_totaal(ma, di, woe, don, vrij, zat, zon):
        inkomsten = sum((ma, di, woe, don, vrij, zat, zon))
        bedrag = inkomsten * 0.09
        uitvoer = f"Het bedrag van alle inkomsten van deze week is {inkomsten} eruo, waarover {bedrag} euro btw betaald dient te worden."
        return uitvoer

def laag_en_hoog(ma, di, woe, don, vrij, zat, zon):
        mijn_lijst = (ma, di, woe, don, vrij, zat, zon)
        hoogste = max(mijn_lijst)
        laagste = min(mijn_lijst)
        return f"De hoogste waarde {hoogste}, de laagste waarde {laagste}."

def gemiddelde(ma, di, woe, don, vrij, zat, zon):
        mijn_lijst = (ma, di, woe, don, vrij, zat, zon)
        gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
        return f"De gemiddelde inkomsten van deze week zijn {gemiddelde} euro."

def meervoudig(ma, di, woe, don, vrij, zat, zon):
        return laag_en_hoog(ma, di, woe, don, vrij, zat, zon)

def combinatie(invoer_lijst_2):
        korte_lijst = laag_en_hoog(invoer_lijst_2)
        uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
        return uitvoer

    
  


print(aanbieding_1("aardbei", 4, 0.1))
print(inkomsten_totaal(220, 430, 125, 160, 205, 90, 345))
print(laag_en_hoog(220, 430, 125, 160, 205, 90, 345))
print(gemiddelde(220, 430, 125, 160, 205, 90, 345))
print(meervoudig(10, 5, 3, 2, 1, 2, 9))


