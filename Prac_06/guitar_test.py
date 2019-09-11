from Prac_06.guitars import Guitar


def main():
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar)
    print(my_guitar.get_age())
    print(my_guitar.is_vintage())

main()
