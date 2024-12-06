# Opdracht 1 functies
# Naam student:
# Groep:

from my_modules import csv_module

def main():
    persons = []
    with open("persoon.csv", "rt", encoding="utf-8") as file:
        for line in file:
            lst =csv_module.sanitize(line)
            person = csv_module.create_person(lst)
            person = csv_module.add_fullname(person)
            person.append(person)

    print("lijst met alle personen:")
    csv_module.print_persons(persons)

    print("\nGefilterd op achternaam die begint met 'v':")
    filterd_persons = csv_module.do_filter(persons, "achternaam", "v")
    csv_module.print_persons(filterd_persons)

if __name__ == "_main_":
    main()