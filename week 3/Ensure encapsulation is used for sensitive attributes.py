#Ensure encapsulation is used for sensitive attributes by the class hierarchy Vehicle → Car and Bike.
class Vehicle:
    def __init__(self, make, model):
        self._make = make  #Protected attribute
        self._model = model  #Protected attribute

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def describe(self):
        return f"Vehicle Make: {self._make}, Model: {self._model}"

#Car subclass with encapsulated num_doors
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors  #Private attribute

    def get_num_doors(self):
        return self.__num_doors

    def set_num_doors(self, doors):
        if doors > 0:
            self.__num_doors = doors
        else:
            print("Number of doors must be positive.")

    def describe(self):
        return f"Car Make: {self.get_make()}, Model: {self.get_model()}, Doors: {self.__num_doors}"

#Bike subclass with encapsulated bike_type
class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.__bike_type = bike_type #Private attribute 

    def get_bike_type(self):
        return self.__bike_type

    def set_bike_type(self, bike_type):
        self.__bike_type = bike_type

    def describe(self):
        return f"Bike Make: {self.get_make()}, Model: {self.get_model()}, Type: {self.__bike_type}"

#Function demonstrating encapsulation and polymorphism
def print_vehicle_info(vehicle):
    print(vehicle.describe())

#Example usage
car = Car("Toyota", "Corolla", 4)
bike = Bike("Harley-Davidson", "Sportster", "Cruiser")

#Accessing encapsulated attributes using getter methods
print(f"Car has {car.get_num_doors()} doors.")
print(f"Bike type is {bike.get_bike_type()}.")

#Modifying encapsulated attributes using setter methods
car.set_num_doors(2)
bike.set_bike_type("Touring")

print_vehicle_info(car)  
print_vehicle_info(bike) 

#Output #Car has 4 doors.
        #Bike type is Cruiser.
        #Car Make: Toyota, Model: Corolla, Doors: 2
        #Bike Make: Harley-Davidson, Model: Sportster, Type: Touring
