#Add a subclass Car that includes num_doors and overrides a describe() method.
class vehicle:
  def _init_(self, make, model):
    self.make = make
    self.model = model

  def _str_self(self):
    return f"vechile make: {self.make}, model: {self.model}"

#Car class hierarchy
class car(vehicle):
  def _init_(self, make, model, num_doors):
    super()._init_(make, model)
    self.num_doors = num_doors

  def describe(self):
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"

#Example usage
car = Car("Toyota", "Camry", 4)
print(car.describe()) 

#Output: Car Make: Toyota, Model: Camry, Doors: 4
