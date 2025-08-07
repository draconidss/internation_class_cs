# class define
class Dog:
    """this is a class of dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print("sit")
    
    def roll_over(self):
        print(f"the dog {self.name} is rolling over")

# create a instance
dog1 = Dog("dog1", 2)
dog2 = Dog("dog2", 10)

# dog1
print(f"the dog1 name is {dog1.name}")
print(f"the dog1 age is {dog1.age}")
dog1.sit()
dog1.roll_over()

# dog2
print(f"the dog2 name is {dog2.name}")
print(f"the dog2 age is {dog2.age}")
dog2.sit()
dog2.roll_over()

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year =year
        self.odometer_reading = 0
        

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
    

# my_car = Car("bmw","m4","2025")
# print(my_car.get_descriptive_name())
# my_car.update_odometer(23)
# my_car.read_odometer()

class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, size=40):        
        """初始化电池的属性"""
        self.size = size
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.size}-kWh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        print(f"This car has a {self.battery.describe_battery()}-kWh battery.")
    def get_descriptive_name(self):
        return f"{super().get_descriptive_name()} {self.battery.describe_battery()}".title()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()


print("\n=============9.1 餐馆=============")
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        print(f"name: {self.name}\ntype: {self.type}")
    def open_restaurant(self):
        print("restaurant is open")

restaurant = Restaurant("a","b")
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
