from car import Car
from utils import create_rental_number, get_rental_date


customer = {"name": "Yuliia", "balance": 1000}

car1 = Car("BMW", "X5", 100)
car2 = Car("Audi", "Q7", 120)
car3 = Car("Volvo", "XC60", 90)

cars = [car1, car2, car3]

for car in cars:
    car.show_info()


selected_car = car2
days = 4

balance_before = customer["balance"]

if selected_car.rent(customer, days):
    rental_number = create_rental_number()
    rental_date = get_rental_date()

    print("Rental successful")
    print("Customer:", customer["name"])
    print("Car:", selected_car.brand, selected_car.model)
    print("Days:", days)
    print("Price:", selected_car.calculate_price(days))
    print("Rental number:", rental_number)
    print("Rental date:", rental_date)
    print("Balance before:", balance_before)
    print("Balance after:", customer["balance"])

else:
    print("Rental failed")
    print("Not enough money")


selected_car.show_info()

selected_car.return_car()

selected_car.show_info()


print(type(car2))
print(isinstance(car2, Car))
print(vars(car2))
print(hasattr(car2, "brand"))
print(getattr(car2, "model"))
print(Car.__doc__)
