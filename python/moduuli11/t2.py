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


class ElectricCar(Car):
    def __init__(self, reg_plate, top_speed, battery_capacity, current_speed=0, travelled_distance=0):
        super().__init__(reg_plate, top_speed, current_speed, travelled_distance)
        self.battery_capacity = battery_capacity


class NormalCar(Car):
    def __init__(self, reg_plate, top_speed, gas_tank, current_speed=0, travelled_distance=0):
        super().__init__(reg_plate, top_speed, current_speed, travelled_distance)
        self.gas_tank = gas_tank


electric_car1 = ElectricCar("ABC-15", 180, 52.5)
normal_car1 = NormalCar("ACD-123", 165, 32.3)

electric_car1.accelerate(110)
normal_car1.accelerate(100)

electric_car1.travel(3)
normal_car1.travel(3)


print(f"Electric car:\nReg plate: {electric_car1.reg_plate}, top speed: {electric_car1.top_speed} km/h, "
      f"current speed: {electric_car1.current_speed} km/h, travelled distance: {electric_car1.travelled_distance} km, "
      f"battery capacity: {electric_car1.battery_capacity} kWh\n")

print(f"Normal car:\nReg plate: {normal_car1.reg_plate}, top speed: {normal_car1.top_speed} km/h, "
      f"current speed: {normal_car1.current_speed} km/h, travelled distance: {normal_car1.travelled_distance} km, "
      f"gas tank: {normal_car1.gas_tank} l\n")
