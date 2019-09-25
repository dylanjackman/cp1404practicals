from Prac_06.guitar import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print("{} get_age() - Expected 97. Got {}".format(my_guitar.name, my_guitar.get_age()))
    another_guitar = Guitar("Fender Stratocaster", 2014, 765.4)
    print("{} get_age() - Expected 5. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(my_guitar.name, my_guitar.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
