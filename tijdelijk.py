Prijzen = {
    "Aardbei" : 3,
    "Vanille" : 4,
    "Chocolade" : 5
}
Aanbieding = Prijzen["Aardbei"] * 0.8
Reclame_tekst = (f"Vandaag in de aanbieding: Vanille-ijs, 1 liter - slechts €{Aanbieding}")
Reclame_tekst2 = Reclame_tekst[:62]
Reclame_tekst3 = Reclame_tekst2.upper()
Reclame_tekst4 = Reclame_tekst3.split()
for el in Reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())
        


    
 
