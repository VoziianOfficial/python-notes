from vehicles import Car, Vehicle, Bike, Scooter

bike = Bike("Trek", "FX 2", 200)
scooter = Scooter("Xiaomi", "Pro 2", 150)
car = Car("BMW", "X5", 100)

vehicles = [car, bike, scooter]

for vehicle in vehicles:
    print(vehicle.__class__.__name__)
    print("Price per day:", vehicle.price_per_day)
    print("3 days:", vehicle.calculate_price(3))
    print()
