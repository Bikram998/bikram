# Inheritance
# Child classes are derived with the properties of base class
# Example:- surname, shape, vehicle, smartphone, human etc

# syntax
# class ParentClass():
#   attributes
#   methods

# class ChildClass(ParentClass):
#   attributes
#   methods

class SmartPhone():
    brand = str
    range = str 
    os = str
    build_material = str

    def getInfo(self):
        print("i am a parent class")

class SamsungPhone(SmartPhone):
    madein = str
    
    def getDetail(self):
        print("I am samsung")

sm = SamsungPhone()
sm.range = "Top end"
sm.os = "Andriod"
sm.brand = "Samsung"

sm.build_material = "Plastic"
sm.madein = "China"
sm.getInfo()
sm.getDetail()

print(sm.brand)
print(sm.build_material)
print("")

# with constructor
class Vehicle():
    def __init__(self, category, engine, brand):
        self.category = category
        self.engine = engine
        self.brand = brand
    
    def info(self):
        print("I am a parent of vehicle")

# if constructor is defined inside child class then parent's class constructor must
# be defined inside child class constructor
# method one by class name. self keyword must be pass
# method two by super() method. no need to pass self keyword

class Car(Vehicle):
    def __init__(self, category, engine, brand, wheel, chasis):
        Vehicle.__init__(self, category, engine, brand)
        self.wheel = wheel
        self.chasis = chasis
    
    def detail(self):
        print("I am a car")

class Bike(Vehicle):
    def __init__(self, category, engine, brand, wheel, chasis):
        super().__init__(category, engine, brand)
        self.wheel = wheel
        self.chasis = chasis
    
    def bikeDetail(self):
        print("I am a bike")

c = Car("4 Wheel", "1000 CC", "Hyudai", "2 Wheel", "Rectangle")
b = Bike("2 Wheel", "250 CC", "Yamaha", "2 Wheel", "One Frame")

print(c.brand)
print(b.brand)

# Types of Inheritance
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multi-level/Hierarchical Inheritance

# 2. Multiple Inheritance
class Shape():
    def info(self):
        print("I am a shape")

class Area():
    def calculateArea(self):
        print("I am a area")

class Perimeter():
    def calculatePerimeter(self):
        print("I am a perimeter")

class Quardilateral():
    def side(self):
        print("I have four side")

class Rectangle(Shape, Area, Perimeter, Quardilateral):
    def detail(self):
        print("I am a rectangle")
        
r1 = Rectangle()
r1.detail()
r1.calculateArea()
r1.calculatePerimeter()
r1.info()
r1.side()
