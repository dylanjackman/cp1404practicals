from Prac_06.guitar import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    if my_guitar.is_vintage():
        print(my_guitar, "\nThis guitar is {} years old which makes this a vintage guitar".format(my_guitar.get_age()))
    else:
        print(my_guitar, "\nThis guitar is {} years old which doesn't make it a vintage.... yet.".format(my_guitar.
                                                                                                         get_age()))


main()
