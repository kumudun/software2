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


class Employee:

    total_employees = 0

    def __init__(self, first_name, last_name):
        Employee.total_employees = Employee.total_employees + 1
        self.employee_number = Employee.total_employees
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"{self.employee_number}: {self.first_name} {self.last_name}")

class HourlyPaid(Employee):

    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Hourly pay: {self.hourly_pay}")

class MonthlyPaid(Employee):

    def __init__(self, first_name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Monthly pay: {self.monthly_pay}")


employees = []
employees.append(HourlyPaid("Viivi", "Virta", 12.35))
employees.append(MonthlyPaid("Ahmed", "Habib", 2750))
employees.append(Employee("Pekka", "Puro"))
employees.append(HourlyPaid("Olga", "Glebova", 14.92))

for e in employees:
    e.print_information()
