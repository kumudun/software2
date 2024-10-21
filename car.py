class Car:
    def __init__(self, reg_num, max_speed, cur_speed = 0, travel_dist = 0):
        self.registration_number = reg_num
        self.maximum_speed = max_speed
        self.current_speed = cur_speed
        self.travelled_distance = travel_dist


    def accelerate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0


    def drive(self,time):
        self.travelled_distance= self.current_speed * time