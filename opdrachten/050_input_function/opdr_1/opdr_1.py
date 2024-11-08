# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.
import math

# Vraag de lengte van de eerste zijde
zijde1 = float(input("Geef de lengte van de eerste zijde: "))

# Vraag de lengte van de tweede zijde
zijde2 = float(input("Geef de lengte van de tweede zijde: "))

# Bereken de schuine zijde met de stelling van Pythagoras
schuine_zijde = math.sqrt(zijde1**2 + zijde2**2)

# Toon de lengte van de schuine zijde
print(f"De lengte van de schuine zijde is: {schuine_zijde}")


