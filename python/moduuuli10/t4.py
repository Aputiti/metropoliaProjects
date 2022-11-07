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


car_list1 = [Car("ABC-" + str(i), rnd.randint(100, 200)) for i in range(1, 11)]


class Race:
    def __init__(self, race_name, race_length_km, participating_cars):
        self.race_name = race_name
        self.race_length_km = race_length_km
        self.participating_cars = participating_cars

    def hour_passes(self):
        for car in car_list1:
            car.accelerate(rnd.randint(-10, 15))
            car.travel(1)

    def print_situation(self):
        for obj in car_list1:
            print(f"Reg plate: {obj.reg_plate}, top speed: {obj.top_speed} km/h, current speed: {obj.current_speed} km/h"
                  f", travelled distance: {obj.travelled_distance} km")
        print("")

    def race_over(self):
        for car in car_list1:
            if car.travelled_distance > self.race_length_km:
                return True


race = Race("Demolition derby", 8000, car_list1)

print(f"Start {race.race_name}!\n\nStarting values:")
for obj in car_list1:
    print(f"Reg plate: {obj.reg_plate}, top speed: {obj.top_speed} km/h, current speed: {obj.current_speed} km/h"
          f", travelled distance: {obj.travelled_distance} km")
print("")
car_racing = True
race_hours_passed = 0
while car_racing:
    race.hour_passes()
    race_hours_passed += 1
    if race_hours_passed % 10 == 0:
        race.print_situation()
    race.race_over()
    if race.race_over():
        car_racing = False
        print("Winner found!")
        race.print_situation()
