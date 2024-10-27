# Fundamentals of object-oriented programming
import random
# Question 1

class Car:
    def __init__(self, regPlate, maxSpeed,):
        
        self.regPlate = regPlate
        self.maxSpeed = maxSpeed
        self.current_speed = 0
        self.odometer = 0

    def accelerate(self,acceleration):
        self.current_speed = min(max(self.current_speed + acceleration, 0), self.maxSpeed)

    def drive(self,time):
        self.odometer += self.current_speed * time


if __name__ == "__main__":
    porsche =Car(regPlate = "ABC-123" , maxSpeed=142)

    print(f"Register plate {porsche.regPlate}, Maximum speed {porsche.maxSpeed}km/h,"
          f"Current speed {porsche.current_speed}km/h,Odometer {porsche.odometer}km")

# Question 2
    porsche.accelerate(30)
    porsche.accelerate(70)
    porsche.accelerate(50)
    print (f"Current speed is {porsche.current_speed}km/h")
    porsche.accelerate(-200)
    print(f"Current speed is {porsche.current_speed}km/h")

# Question 3
    porsche.accelerate(60)
    porsche.drive(1.5)
    print(f"Distance travelled is {porsche.odometer}km")

# Question 4
    cars =[]
    for i in range (10):
        cars.append(Car("ABC-" + str(i+1), random.randint(100,200)))

    distance_max =0.
    while distance_max < 10000:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1.)
            distance_max = max(car.odometer, distance_max)

    for car in cars:
        print(f"{car.regPlate},"
              f"{car.maxSpeed} , {car.current_speed}")





















