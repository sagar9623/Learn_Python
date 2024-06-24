# A very basic class would look something like this:
class MyClass:
    variable = "You are so beautiful and elegent looking girl"
    def function(self):
        print("This is a message inside the class.")

my_object = MyClass()
print(my_object.variable)

my_object.function()

# EXample

class Car:
    # class variable
    wheel = 4

    # Constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Method / Function
    def drive(self):
        print("The", self.make, self.model, "is driving")

# Create instances of the Car class outside the class definition    
car1 = Car("BMW", "M5 Turbo Charge")
car2 = Car("Lamborghini", "Urus")

# Call the drive method on the instances("Method Calls")
car1.drive()
car2.drive()

class Vehicle:
    
    def __init__(self, name, kind="car", color="", value=100.00):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        dec_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return dec_str

car1 = Vehicle("Ferrari", "sports car", "red", 60000.00)
car2 = Vehicle("Tesla", "electric car", "white", 75000.00)

print(car1.description())
print(car2.description())