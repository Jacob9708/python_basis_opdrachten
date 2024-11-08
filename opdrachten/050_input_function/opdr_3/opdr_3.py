# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
# Vraag de gebruiker om een lijst van minimaal 5 items in te voeren, gescheiden door komma's
items = input("Vul minimaal 5 items in, gescheiden door een komma (bijv. steden: Amsterdam, Zwolle, Dronten, Haarlem, Zaanstad): ")

# Verdeel de items op basis van komma's en verwijder eventuele extra spaties
lijst = [item.strip() for item in items.split(",")]

# Sorteer de lijst in omgekeerde alfabetische volgorde
lijst.sort(reverse=True)

# Print de gesorteerde lijst
print(lijst)

