from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Hummer", 200, 4)
    my_taxi.drive(49)
    print(my_taxi)
    print("${}".format(my_taxi.get_fare()))


main()
