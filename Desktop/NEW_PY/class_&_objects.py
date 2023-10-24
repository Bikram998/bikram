# Class and object
# class - blueprint of object
# Object - instance of class

# syntax
# class ClassName():
#    attributes
#    methods

# Class Name - common or collective noun
# Attributes - characteristics of Class(Adjective)
# Methods - action of class (Verb)


class person():
    gender = "Male"
    dob = "1997-09-14"
    name = "Maila Kumar"


    def walk(self):
        print("I can walk")

    def breadth(self):
        print("I can breathe")

    def eat(self):
        print("I can eat")

class vehicle():
    engine ="1000 cc"
    brand= "Honda"
    chasis = "4Frame"
    wheel = "4 Wheel and tubes"
    rim = "spark"
    brake = "Dark and drum"

    def brake(self):
        print("I am brake and i stop vehicle")

    def accelerate():
        print("My job is to accelerate the vehicle movement")
    

    

# accesing attributes by class name

print(person.breadth)
print(person.dob)
print(person.eat)
print(vehicle.accelerate)
print(vehicle.brand)
print(vehicle.brake)
print(vehicle.chasis)


# accessing attributes and methods byb creating object
# syntax
# obj_name = ClassName()

# object of person
p1 = person()
print(id(p1))  # checking object id in memory
print(p1)  # checking object memory reference


print("")

print(p1.breadth)
print(person.dob)
print(person.gender)

# object of vehicle 
v1 = vehicle()
print(v1.accelerate)
print(v1.brake)
print(v1.brand)
print(v1.engine)

v1.accelerate
v1.brake
print("")

# storing values in class attributes
v1.engine = "1200cc"
v1.brand = "suzuki"
print(v1.brand)
print(v1.engine)
v1.brake = "I am braking"
print(v1.brake)

# self :- is a userdefined keywords which indicates that the attributes and methods
# belongs to that particular class where they are defined
# it is passed as an argument in function and is used before attribute name
# example:

#def getName(self):
#   return self.name
# method vs function:- 


