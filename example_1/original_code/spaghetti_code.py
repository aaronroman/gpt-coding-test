

# car 1
def define_car_1():
    vehicle = {"name": None,
            "motor": None,
            "color": None,
            "year": None,
            "mileage": None,
            "price": None}

    car1 = vehicle.copy()
    car1['name'] = 'Toyota'
    car1['color'] = 'red'
    car1["motor"] = ["electric"]
    car1['year'] = 2015
    car1['mileage'] = 10000
    car1['price'] = 10000

    return car1

def define_car_2():
    vehicle = {"name": None,
            "motor": None,
            "color": None,
            "year": None,
            "mileage": None,
            "price": None}
    
    car2 = vehicle.copy()
    car2['name'] = 'BMW'
    car2['motor'] = ['gas']
    car2['color'] = 'black'
    car2['year'] = 2017
    car2['mileage'] = 20000
    car2['price'] = 20000

    return car2


def check_ecofriendly(car):
    if car['motor'] == ['electric']:
        return True
    return False

if __name__ == '__main__':
    car1 = define_car_1()
    car2 = define_car_2()

    for car in [car1, car2]:
        print(f"Lets check if {car['name']} is eco friendly", end=" -> ")
        print(check_ecofriendly(car))
