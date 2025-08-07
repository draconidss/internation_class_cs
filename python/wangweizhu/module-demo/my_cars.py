from car import Car, ElectricCar
from random import randint

my_new_car = Car('audi', 'a4', 2023)
print(my_new_car.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
