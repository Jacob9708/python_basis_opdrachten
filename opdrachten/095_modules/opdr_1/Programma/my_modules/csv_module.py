def sanitize(line):
    """Zet de inhoud van een CSV-regel in kleine letters en verwijdert overtollige spaties."""
    new_lst = []
    lst = line.split(',')
    for item in lst:
        new_lst.append(item.lower().strip())
    return new_lst


def create_person(lst):
    """Converteert een lijst naar een dictionary met persoongegevens."""
    return {
        "voornaam": lst[0],
        "tussenvoegsel": lst[1],
        "achternaam": lst[2],
        "adres": lst[3],
        "postcode": lst[4],
        "plaats": lst[5],
    }


def add_fullname(person):
    """Voegt een volledige naam toe aan een persoon."""
    if person["tussenvoegsel"] == "":
        person["full_name"] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person["full_name"] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person


def print_persons(persons, filter_keys=["full_name"]):
    """Print gegevens van personen en toont het totaal aantal."""
    counter = 0
    for person in persons:
        counter += 1
        for key in filter_keys:
            print(person[key], end=" ")
        print()
    print(f"Er zijn in totaal {counter} personen.")


def do_filter(persons, field, value):
    """Filtert personen op een specifiek veld dat begint met een waarde."""
    filtered = [
        person for person in persons if person[field].lower().startswith(value.lower())
    ]
    return filtered
