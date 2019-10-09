from Prac_08.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print("Taxi name: {}, Current Fuel {} and Current Fare is ${}".format(my_taxi.name, my_taxi.fuel,
                                                                          my_taxi.get_fare()))

    my_taxi.start_fare()
    my_taxi.drive(100)
    print("Taxi name: {}, Current Fuel {} and Current Fare is ${}".format(my_taxi.name, my_taxi.fuel,
                                                                          my_taxi.get_fare()))


main()
