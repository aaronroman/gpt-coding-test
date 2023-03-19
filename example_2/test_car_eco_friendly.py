import unittest
from car import Car
from eco_friendly import EcoFriendlyChecker


class TestCarEcoFriendlyChecker(unittest.TestCase):

    def test_car_creation(self):
        car = Car(name='Toyota', motor=['electric'], color='red', year=2015, mileage=10000, price=10000)
        self.assertEqual(car.name, 'Toyota')
        self.assertEqual(car.motor, ['electric'])
        self.assertEqual(car.color, 'red')
        self.assertEqual(car.year, 2015)
        self.assertEqual(car.mileage, 10000)
        self.assertEqual(car.price, 10000)

    def test_eco_friendly_checker(self):
        car1 = Car(name='Toyota', motor=['electric'], color='red', year=2015, mileage=10000, price=10000)
        car2 = Car(name='BMW', motor=['gas'], color='black', year=2017, mileage=20000, price=20000)

        eco_friendly_checker = EcoFriendlyChecker()

        self.assertTrue(eco_friendly_checker.check_eco_friendly(car1))
        self.assertFalse(eco_friendly_checker.check_eco_friendly(car2))


if __name__ == '__main__':
    unittest.main()
