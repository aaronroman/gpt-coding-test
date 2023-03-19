from dataclasses import dataclass
from typing import List


# Defining the 'Car' dataclass to store car information
@dataclass
class Car:
    name: str
    motor: List[str]
    color: str
    year: int
    mileage: int
    price: int
