# Car and EcoFriendlyChecker Documentation

This script provides two classes, `Car` and `EcoFriendlyChecker`, which can be used for storing car information and checking if a car is environmentally friendly, respectively. The classes can be reused in other programs as needed.

## Car Class

The Car class is a simple dataclass used for storing car information. It has the following attributes:

- `name` (str): The name of the car.
- `motor` (List[str]): A list containing the type of motor the car uses, e.g., `['electric']`, `['gas']`.
- `color` (str): The color of the car.
- `year` (int): The year the car was manufactured.
- `mileage` (int): The car's mileage.
- `price` (int): The price of the car.

#### Usage

To create a new Car object, simply pass in the required attributes:

```
car1 = Car(name='Toyota', motor=['electric'], color='red', year=2015, mileage=10000, price=10000)
```

## EcoFriendlyChecker Class

The `EcoFriendlyChecker` class provides a method to check if a car is environmentally friendly.

#### Methods

`check_eco_friendly(car: Car) -> bool`
This method takes a `Car` object as input and returns a boolean value indicating whether the car is environmentally friendly or not.

A car is considered environmentally friendly if its motor type is 'electric'.

#### Parameters

- `car` (Car): An object of the Car class.
- 

#### Returns

- `True` if the car is environmentally friendly, False otherwise.

#### Usage

To use the `EcoFriendlyChecker` class, first create an instance of the class:

```
eco_friendly_checker = EcoFriendlyChecker()
```

Then, call the `check_eco_friendly` method with a Car object:

```
is_eco_friendly = eco_friendly_checker.check_eco_friendly(car1)
```

### Example

The following example demonstrates how to use both the `Car` and `EcoFriendlyChecker` classes:

```
from car import Car
from eco_friendly import EcoFriendlyChecker

car1 = Car(name='Toyota', motor=['electric'], color='red', year=2015, mileage=10000, price=10000)
car2 = Car(name='BMW', motor=['gas'], color='black', year=2017, mileage=20000, price=20000)

eco_friendly_checker = EcoFriendlyChecker()

for car in [car1, car2]:
    print(f"Lets check if {car.name} is eco friendly", end=" -> ")
    print(eco_friendly_checker.check_eco_friendly(car))

```

Output:

```
Lets check if Toyota is eco friendly -> True
Lets check if BMW is eco friendly -> False
```