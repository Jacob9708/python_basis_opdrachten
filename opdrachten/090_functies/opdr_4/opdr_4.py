# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        voornaam = naam["voornaam"]
        tussenvoegsel = naam["tussenvoegsel"]
        achternaam = naam["achternaam"]

        
        if tussenvoegsel:
            print(f"{voornaam} {tussenvoegsel} {achternaam}")
        else:
            print(f"{voornaam} {achternaam}")


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Functie aanroepen
volledige_naam(namen)
