# Question 1

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"Elevator is moving from {self.current} to {self.current + 1}")
            self.current += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is moving from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            return False

    def go_to_floor(self,floor):
        if floor >self.current:
            for i in range (floor-self.current):
                if not self.floor_up():
                    break
        elif floor <self.current:
            for i in range (self.current-floor):
                if not self.floor_down():
                    break
        else:
            print(f"Elevator is already at the requested floor{self.current}")

kara_elevator = Elevator(1, 7)
target_floor = int(input("Which floor do you want to go to? : "))
kara_elevator.go_to_floor(target_floor)
kara_elevator.go_to_floor(1)

# Question 2 and 3

class Building:
    def __init__(self,bottom, top, elevators):
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        print(f"Elevator {elevator_num} is moving")
        self.elevators[elevator_num - 1].go_to_floor(floor)

    def fire_alam(self):
        print("Fire alam is ringing")
        for e in self.elevators:
            e.go_to_floor(e.bottom)

print("\n Elevators in the building:")
building1 = Building(1, 7,elevators=3)
building1.run_elevator(1,4)
building1.run_elevator(2,2)
building1.run_elevator(3,7)
building1.fire_alam()

# Question 4
from exercise9 import Car

class Race:
    def __init__(self,name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passed(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1.)

    def print_stats(self):
        print(self.name + ":")
        print("Reg Plate Speed Odometer")
        print("------------------------")
        for car in self.cars:
            print(f"{car.regPlate:6s}:{car.currentSpeed:3d}km/h , {car.odometer}")

    def race_finished(self):
        for car in self.cars:
            if car.odometer >= self.distance:
                return True
            return False

cars =[]
for car in range(10):
    cars.append(Car("ABC-"+str(i+1), random.randint(100,200)))

race = Race("Grand Demolition Derby", 8000, cars)
n=0
while not race.race_finished():
    race.hour_passed()
    n+=1
    if n % 10 ==0:
        print(f"After {n} hours")
        race.print_stats()









