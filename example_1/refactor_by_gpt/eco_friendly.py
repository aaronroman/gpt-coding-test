from car import Car


# Define the EcoFriendlyChecker class to check if a car is environmentally friendly.
class EcoFriendlyChecker:
    @staticmethod
    def check_eco_friendly(car: Car) -> bool:
        """
        Check if a car is environmentally friendly.

        :param car: An object of the Car class.
        :return: True if the car is environmentally friendly, False otherwise
        """
        if car.motor == ['electric']:
            return True
        return False
