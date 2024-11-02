  # Question 1
class Publication:
     def __init__(self, name):
         self.name = name

     def print_info(self):
         print(self.name, end=" ")

class Book(Publication):
    def __init__(self, name,author,pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
    def print_info(self):
        super().print_info()
        print("(author"+ self.author+ " "+ str(self.pages)+ "pages)")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print("editor"+ self.editor)

pub = []
pub.append(Magazine("Donald Duck","Aki Hyppa"))
pub.append(Book("Compartment No.6","Rosa Likson", 192))
for i in pub:
    i.print_info()

# Question 2
from exercise9 import Car

class ElectricCar(Car):
    def __init__(self, regPlate, maxSpeed, battery_capacity):
        super().__init__(regPlate, maxSpeed)
        self.battery_capacity = battery_capacity

    def print_odometer(self):
        print("Odometer: " + str(self.odometer))


class GasolineCar(Car):
      def __init__(self, regPlate, maxSpeed, tank_capacity):
          super().__init__(regPlate, maxSpeed)
          self.tank_capacity = tank_capacity

      def print_odometer(self):
          print("Odometer: " + str(self.odometer))

el_car1 = ElectricCar("ABC-15", 180, 68.5)
gas_car1 = GasolineCar("ACD-40", 170, 35)
el_car1.accelerate(30.)
gas_car1.accelerate(100.)
el_car1.drive(3.); gas_car1.drive(3.)
el_car1.print_odometer(); gas_car1.print_odometer()


