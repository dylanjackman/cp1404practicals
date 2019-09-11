"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("Fuel =", my_car.fuel)
    print("Odo =", my_car.odometer)
    print(my_car, "\n")

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}\n".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("Fuel =", limo.fuel)
    limo.drive(115)
    print("Odo =", limo.odometer)
    print(limo)


main()
