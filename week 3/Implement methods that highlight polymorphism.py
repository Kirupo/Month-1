#Implement methods that highlight polymorphism by the class hierarchy Vehicle → Car and Bike.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"

#Car class heriarchy
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"

#Bike class hierarchy
class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.bike_type = bike_type

    def describe(self):
        return f"Bike Make: {self.make}, Model: {self.model}, Type: {self.bike_type}"

#Function demonstrating polymorphism
def print_vehicle_info(vehicle):
    print(vehicle.describe())

#Example usage
car = Car("Honda", "Accord", 4)
bike = Bike("Harley-Davidson", "Sportster", "Cruiser")

#Demonstrating polymorphism
print_vehicle_info(car)  
print_vehicle_info(bike) 

#Output #Car Make: Honda, Model: Accord, Doors: 4
        #Bike Make: Harley-Davidson, Model: Sportster, Type: Cruiser
