# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...
gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print(gasten)

gasten.remove("Marie")
print(gasten)

kees_index = gasten.index("Kees")  
gasten.insert(kees_index + 1, "George")  
print(gasten)
