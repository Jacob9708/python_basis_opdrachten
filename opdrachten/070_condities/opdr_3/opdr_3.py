# Opdracht 3 condities
# Naam student:Jacob van de Berg
# Groep:

#code:
normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijdsgroepen = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}


def bepaal_leeftijdsgroep(leeftijd):
    for groep, (min_leeftijd, max_leeftijd) in leeftijdsgroepen.items():
        if min_leeftijd <= leeftijd <= max_leeftijd:
            return groep
    return None  

try:
    bezoeker_leeftijd = int(input("Wat is de leeftijd van de bezoeker? "))
    groep = bepaal_leeftijdsgroep(bezoeker_leeftijd)  

    if groep is not None:  
        korting = kortings_percentages[groep]
        prijs = normale_toegangsprijs * (1 - korting / 100)
        print(f"De toegangsprijs voor een {groep} ({bezoeker_leeftijd} jaar oud) is €{prijs:.2f}.")
    else:
        print("De ingevoerde leeftijd valt niet binnen een bekende leeftijdscategorie.")
except ValueError:
    print("Ongeldige invoer. Voer een getal in voor de leeftijd.")