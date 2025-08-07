"""a class represtent car"""

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

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        print(f"This car has a {self.battery.describe_battery()}-kWh battery.")
    def get_descriptive_name(self):
        return f"{super().get_descriptive_name()} {self.battery.describe_battery()}".title()

class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, size=40):        
        """初始化电池的属性"""
        self.size = size
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.size}-kWh battery.")