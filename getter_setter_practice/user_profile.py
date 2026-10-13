class UserProfile:
    def __init__(self, name, age):
        self.name = name
        self.__age = 0
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            return
        
        elif value > 120:
            return 
        else:
            self.__age = value