#Create a Vehicle class with attributes make and model.
class vehicle:
  def _init_(self, make, model):
    self.make = make
    self.model = model

  def _str_self(self):
    return f"vechile make: {self.make}, model: {self.model}"

#Example usage 
car = vehicle("Honda", "civic")
print(car)

#Output vechile make: Honda, model: Civic
