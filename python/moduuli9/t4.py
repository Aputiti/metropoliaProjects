import random as rnd

class Car:
    def __init__(self, reg_plate, top_speed, current_speed=0, travelled_distance=0):
        self.reg_plate = reg_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed

    def travel(self, hr):
        if hr > 0:
            distance_change = self.current_speed * hr
            self.travelled_distance += distance_change
        else:
            print("SET A POSITIVE TRAVEL TIME!\n")


car_list = [Car("ABC-" + str(i), rnd.randint(100, 200)) for i in range(1, 11)]

print("Starting values:")
for obj in car_list:
    print(f"Reg plate: {obj.reg_plate}, top speed: {obj.top_speed} km/h, current speed: {obj.current_speed} km/h"
          f", travelled distance: {obj.travelled_distance} km")

car_racing = True
while car_racing:
    for car in car_list:
        car.accelerate(rnd.randint(-10, 15))
        car.travel(1)
        if car.travelled_distance > 10000:
            car_racing = False

print("\nRace finished, there is a winner:")
for obj in car_list:
    print(f"Reg plate: {obj.reg_plate}, top speed: {obj.top_speed} km/h, current speed: {obj.current_speed} km/h"
          f", travelled distance: {obj.travelled_distance} km")
