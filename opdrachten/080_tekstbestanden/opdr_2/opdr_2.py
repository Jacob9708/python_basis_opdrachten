# Opdracht 2 tekstbestanden
# Naam student:Jacob van de Berg
# Groep:

import random
prompt = "Raad mijn Geheime getal \n"
geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

print("Welkom bij Raad het getal'!")
print("Ik heb een getal gekozen tussen 1 en de 100. Kun jij raden wat het is?")

while True:
    try:
        gok = int(input("Voer je gok in:"))
        aantal_pogingen += 1

        if gok < geheim_getal:
            print("Hoger!")
        elif gok > geheim_getal:
            print("Lager!")
        else:
            print(f"Gefeliciteerd je hebt het geraden!!")
            print(f"Het duurde {aantal_pogingen} pogingen om het getal te raden!")

    except ValueError:
        print("Ongeldige invoer probeer een heel getal in te voeren.")
                  
    


