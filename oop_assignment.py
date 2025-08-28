# oop_assignment.py
# Author: Wycliffe
# Date: 28/08/2025
# Assignment: OOP Assignment


# Assignment 1: Design Your Own Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # in mAh

    def call(self, contact):
        return f"{self.brand} {self.model} is calling {contact}..."

    def charge(self, amount):
        self.battery += amount
        return f"Battery charged. Current battery: {self.battery}mAh"

# Inheritance: add a subclass
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    # Example of polymorphism (method override)
    def call(self, contact):
        return f"{self.brand} {self.model} (Gaming Mode 🎮) is calling {contact}..."

    def play_game(self, game):
        return f"Playing {game} smoothly with {self.gpu} GPU!"

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Testing the Classes

if __name__ == "__main__":
    # Assignment 1 test
    phone = Smartphone("Samsung", "Galaxy S24", "256GB", 5000)
    print(phone.call("Alice"))
    print(phone.charge(500))

    g_phone = GamingPhone("Asus", "ROG 7", "512GB", 6000, "Adreno 730")
    print(g_phone.call("Bob"))
    print(g_phone.play_game("Call of Duty Mobile"))

    # Activity 2 test
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
