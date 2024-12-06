# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(filename, text):
    """
    Schrijft tekst naar een bestand. Als het bestand al bestaat,
    wordt de tekst toegevoegd aan de inhoud.

    Parameters:
    filename (str): De naam van het bestand.
    text (str): De tekst die moet worden weggeschreven.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        print(f"Tekst succesvol toegevoegd aan {filename}.")
    except Exception as e:
        print(f"Er is een fout opgetreden bij het schrijven naar {filename}: {e}")

bestandsnaam = input("Voer de naam van het bestand in (bijv. 'test.txt'): ")
while True:
    tekst = input("Voer de tekst in die je wilt toevoegen: ")

    write_to_file(bestandsnaam, tekst)

    doorgaan = input("Wil je meer tekst toevoegen? (ja/nee): ").strip().lower()
    if doorgaan != "ja":
        print("Programma beëindigd.")
        break
