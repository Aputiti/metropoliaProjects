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


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.travel(1.7)

print(f"Car1 reg plate: {car1.reg_plate:s}\nCar1 top speed: {car1.top_speed:d} km/h\n"
      f"Car1 current speed: {car1.current_speed:d} km/h\nCar1 travelled distance: {car1.travelled_distance:.2f} km")

car1.accelerate(-50)
car1.travel(1)

print("\nValues updated!\n")
print(f"Car1 reg plate: {car1.reg_plate:s}\nCar1 top speed: {car1.top_speed:d} km/h\n"
      f"Car1 current speed: {car1.current_speed:d} km/h\nCar1 travelled distance: {car1.travelled_distance:.2f} km")
