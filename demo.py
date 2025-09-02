from abc import ABC, abstractmethod

class Dog:
    def __init__(self, name , age, gender):
        self.name = name # public
        self._age = age # protected
        self.__gender = gender # private
    def sit(self): # self is dog_1 when dog_1 invoke sit
        print(self.name + " is sitting")

    def roll_over(self):
        print(self.name + " is  rolling over")

# Dog_dog_1.__gender

dog_1 = Dog("samoye", 2, "male")
dog_1.name = "xxxx"
dog_1._age = "100"
print(dog_1._Dog__gender)
dog_1.sit()

print()
print()

# parent class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# child class EltricaCar extend Car
class EltricaCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    def __init__(self, size=40):
        self.size = size
    def get_battery_size(self):
        print(f"current battery size is {self.size}")
        
my_leaf = EltricaCar("nissan", "my_leaf", 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery_size = 60
my_leaf.battery.get_battery_size() # current battery size is 60

class Animal(ABC):
    @abstractmethod
    def info(self):
        print("Animal")

class Bird(Animal):
    def demo():
        pass

    # # 实现抽象方法
    # def info(self):
    #     # 调用基类方法(即便是抽象方法)
    #     super().info()
    #     print("Bird")

bird = Bird()
bird.demo()
