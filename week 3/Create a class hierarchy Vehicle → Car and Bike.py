#Create a class hierarchy Vehicle → Car and Bike.
class vehicle:
  def _init_(self, make, model):
    self.make = make
    self.model = model

  def _str_self(self):
    return f"vechile make: {self.make}, model: {self.model}"

#Car class hierarchy
class car(vehicle):
  def _init_(self, make, model, doors):
    super()._init_(make, model)
    self.doors = doors

  def display_info(self):
      super().display_info()
      print(f"Number of Doors: {self.doors}")

#Bike class hierarchy
class bike(vehicle):
  def _init_(self, make, model, biketype):
    super()._init_(make, model)
    self.biketype = bike_type

  def display_info(self):
      super().display_info()
      print(f"bike type: {self.bike_type}")

#Example usage
car = Car("Honda", "Civic", 4)
bike = Bike("Harley-Davidson", "Street 750", "Cruiser")  

car.display_info()
print()
bike.display_info()

#Output #Vehicle Make: Honda, Model: Civic Number of Doors: 4  
        #Vehicle Make: Harley-Davidson, Model: Street 750 Bike Type: Cruiser




