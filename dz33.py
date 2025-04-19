class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Тварина видає звук"

    def display_info(self):
        return f"Тварина: {self.name}, Вид: {self.species}"

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, "Собака")
        self.breed = breed
        self.age = age

    def make_sound(self):
        return "Гав!"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Порода: {self.breed}, Вік: {self.age} років"

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, "Кіт")
        self.breed = breed
        self.age = age

    def make_sound(self):
        return "Мяу!"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Порода: {self.breed}, Вік: {self.age} років"

dog = Dog("Бобі", "Німецька овчарка", 3)
cat = Cat("Мурчик", "Перський", 2)

print(dog.display_info())
print(dog.make_sound())

print(cat.display_info())
print(cat.make_sound())
