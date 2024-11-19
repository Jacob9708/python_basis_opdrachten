# Opdracht 1 while-loops
# Naam student:Jacob van de Berg
# Groep:


import os  

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]


antwoorden = {}

for vraag in vragen:
    antwoord = input(f"{vraag}\n")
    antwoorden[vraag] = antwoord

bureaublad = os.path.join(os.path.expanduser("~"), "Desktop")
bestandspad = os.path.join(bureaublad, "enquete_resultaten.txt")

try:
    with open(bestandspad, "w") as bestand:
        bestand.write("Enquête resultaten:\n")
        bestand.write("=" * 20 + "\n")
        for vraag, antwoord in antwoorden.items():
            bestand.write(f"{vraag}\nAntwoord: {antwoord}\n\n")
    print(f"De resultaten zijn opgeslagen op uw bureaublad in het bestand '{bestandspad}'.")
except IOError:
    print("Er is een fout opgetreden bij het opslaan van de resultaten.")
