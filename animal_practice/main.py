from animals import Animal, Cat, Dog, Cow

cat = Cat("Whiskers", 3, True)
dog = Dog("Buddy", 4, "Golden Retriever")
cow = Cow("Milkshake", 2, 5)


animals = [cat, dog, cow]

for animal in animals:
    animal.show_info()
    animal.make_sound()
    print()


def introduce_animal(animal):
    animal.show_info()
    animal.make_sound()
    print()


introduce_animal(cat)
introduce_animal(dog)
introduce_animal(cow)