from dataclasses import dataclass
from typing import List


# Define la dataclass Car para almacenar la información de los coches
@dataclass
class Car:
    name: str
    motor: List[str]
    color: str
    year: int
    mileage: int
    price: int
