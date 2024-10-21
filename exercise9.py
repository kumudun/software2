# Fundamentals of object-oriented programming

# Question 1

from car import Car

car1 = Car('ABC-123',142)

print (f"""
registration number: {car1.registration_number}
maximum speed: {car1.maximum_speed}
current speed: {car1.current_speed}
travelled distance: {car1.travelled_distance}
""")

# Question 2

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(f"current speed: {car1.current_speed}km/h")

car1.accelerate(-200)
print(f"current speed: {car1.current_speed}km/h")

# Question 3

car1.accelerate(50)
car1.drive(1.5)
print(f"travelled distance: {car1.travelled_distance}km/h")

# Question 4



