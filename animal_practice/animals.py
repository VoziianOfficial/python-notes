class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print("Unknown sound")



class Cat(Animal):
    def __init__(self, name, age, sterilized):
        super().__init__(name, age)
        self.sterilized = sterilized

    def make_sound(self):
        print("Meow")

    def show_info(self):
        super().show_info()
        print(f"Sterilized: {self.sterilized}")



class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print("Woof")

    def show_info(self):
        super().show_info()
        print(f"Breed: {self.breed}")



class Cow(Animal):
    def __init__(self, name, age, milk_per_day):
        super().__init__(name,age)
        self.milk_per_day = milk_per_day

    def make_sound(self):
        print("Moo")

    def show_info(self):
        super().show_info()
        print(f"Milk per day: {self.milk_per_day}")