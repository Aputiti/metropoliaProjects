class Car:
    def __init__(self, reg_plate, top_speed, current_speed=0, travelled_distance=0):
        self.reg_plate = reg_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


car1 = Car("ABC-123", 142)

print(f"Car1 reg plate: {car1.reg_plate:s}\nCar1 top speed: {car1.top_speed:d} km/h\n"
      f"Car1 current speed: {car1.current_speed:d} km/h\nCar1 travelled distance: {car1.travelled_distance:d} km")
