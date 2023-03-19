from car import Car
from eco_friendly import EcoFriendlyChecker


if __name__ == '__main__':
    # Define cars using the Car dataclass.
    car1 = Car(name='Toyota', motor=['electric'], color='red', year=2015, mileage=10000, price=10000)
    car2 = Car(name='BMW', motor=['gas'], color='black', year=2017, mileage=20000, price=20000)

    # Crea una instancia de EcoFriendlyChecker
    eco_friendly_checker = EcoFriendlyChecker()

    for car in [car1, car2]:
        print(f"Lets check if {car.name} is eco friendly", end=" -> ")
        print(eco_friendly_checker.check_eco_friendly(car))
