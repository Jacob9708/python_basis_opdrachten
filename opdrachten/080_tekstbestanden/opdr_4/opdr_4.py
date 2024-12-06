# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:

import os
vragen = [
    "wat is je voornaam?",
    "wat is je achternaam?",
    "wat neem je mee voor drank?",
    "wat neem je mee voor eten?"
]

def verzamel_gegevens():
    antwoorden = {}

    print("beantwoord de volgende vragen:")
    for i, vraag in enumerate(vragen, start=1):
        print(f"{i,} {vraag}")
        antwoord = input(f"Antwoord op vraag {i}:")
        antwoorden[vraag] = antwoord

    return antwoorden

bureaublad = os.path.join(os.path.expanduser("~"), "Desktop")
bestand = os.path.join(bureaublad, "feestgangers.txt")

bestand = "feestgangers.txt"
with open (bestand, "a", encoding="utf-8") as f:
    while True:
        print("\nNieuwe feestgangers invoeren:")
        gegevens = verzamel_gegevens()
        f.write(f"{gegevens}\n")
        doorgaan = input("wil je nog een feestganger invoeren?: (ja/nee):").strip().lower()
        if doorgaan != "ja":
            print("invoer voltooid.")
            break

print(f"De gegevens zijn opgeslagen in {bestand}.")