from Prac_06.guitar import Guitar


def main():
    list_of_guitars = []

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        list_of_guitars.append(guitar_to_add)
        print(guitar_to_add, "added.\n")
        name = input("Name: ")

    # list_of_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # list_of_guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    if list_of_guitars:
        print("\nThese are mine, you are not allowed to touch. But you may look")
        for i, guitar in enumerate(list_of_guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {} ({}), worth ${} {}".format(i, guitar.name, guitar.year, guitar.cost,
                                                            vintage_string))
    else:
        print("Why you no have guitar, go go go and get one!")


main()
