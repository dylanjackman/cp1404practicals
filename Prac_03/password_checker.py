minimum_length = 4


def main():
    password = get_password(minimum_length)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Please enter a password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Please enter a password of at least {} characters: ".format(minimum_length))
    return password


def method_name():
    global print_asterisks

    def print_asterisks(sequence):
        print('*' * len(sequence))


method_name()


main()
