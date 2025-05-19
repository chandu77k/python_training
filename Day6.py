# 1. Employee Hierarchy
class Employee:
    def calculate_bonus(self):
        return 0

class Manager(Employee):
    def calculate_bonus(self):
        return 1000

class Developer(Employee):
    def calculate_bonus(self):
        return 700

class Intern(Employee):
    def calculate_bonus(self):
        return 300

employee_list = [Manager(), Developer(), Intern()]
for emp_instance in employee_list:
    print(f"{emp_instance.__class__.__name__} Bonus: {emp_instance.calculate_bonus()}")


# 2. Vehicle Fleet
class Vehicle:
    def get_max_speed(self):
        return 0

    def print_vehicle_info(self):
        print(f"{self.__class__.__name__} max speed: {self.get_max_speed()} km/h")

class Car(Vehicle):
    def get_max_speed(self):
        return 180

class Truck(Vehicle):
    def get_max_speed(self):
        return 120

class Motorcycle(Vehicle):
    def get_max_speed(self):
        return 200

vehicle_fleet = [Car(), Truck(), Motorcycle()]
for vehicle_obj in vehicle_fleet:
    vehicle_obj.print_vehicle_info()


# 3. Shape Area Calculator
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        return math.pi * self.rad ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h

shape_list = [Circle(3), Rectangle(4, 5), Triangle(6, 4)]
for shape_obj in shape_list:
    print(f"{shape_obj.__class__.__name__} Area: {shape_obj.area():.2f}")


# 4. Notification System
class Notification:
    def send_notification(self):
        pass

class EmailNotification(Notification):
    def send_notification(self):
        print("Sending Email notification")

class SMSNotification(Notification):
    def send_notification(self):
        print("Sending SMS notification")

class PushNotification(Notification):
    def send_notification(self):
        print("Sending Push notification")

def notify_all(notif_list):
    for notif in notif_list:
        notif.send_notification()

notify_all([EmailNotification(), SMSNotification(), PushNotification()])


# 5. Payment Gateway
class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")

class CryptoCurrency(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Crypto.")

def checkout(method, amt):
    method.pay(amt)

checkout(CreditCard(), 1000)
checkout(PayPal(), 2500)
checkout(CryptoCurrency(), 5000)


# 6. Zoo Animal Sounds
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bow!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

zoo_animals = [Dog(), Cat(), Cow()]
for animal_obj in zoo_animals:
    animal_obj.make_sound()


# 7. Custom Range Generator
class MyRange:
    def __init__(self, begin, stop):
        self.current = begin
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

for item in MyRange(1, 6):
    print(item, end=" ")


# 8. Fibonacci Sequence Iterator
class Fibonacci:
    def __init__(self, max_limit):
        self.max_limit = max_limit
        self.x, self.y = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.x <= self.max_limit:
            result = self.x
            self.x, self.y = self.y, self.x + self.y
            return result
        else:
            raise StopIteration

for value in Fibonacci(50):
    print(value, end=" ")


# 9. Reverse String Iterator
class ReverseString:
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = len(input_text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.position > 0:
            self.position -= 1
            return self.input_text[self.position]
        else:
            raise StopIteration

for character in ReverseString("Python"):
    print(character, end=" ")
