class Elevator:
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = lowest_floor

    def move_to_floor(self, floor_target):
        if self.current_floor < floor_target and (self.lowest_floor <= floor_target <= self.highest_floor):
            print("Going up:")
            for i in range(floor_target - self.current_floor):
                self.floor_up()
            print(f"Target (floor {floor_target}) reached!\n")
        elif self.current_floor > floor_target and (self.lowest_floor <= floor_target <= self.highest_floor):
            print("Going down:")
            for i in range(self.current_floor - floor_target):
                self.floor_down()
            print(f"Target (floor {floor_target}) reached!\n")
        elif floor_target < self.lowest_floor:
            print("Error! Your target floor is lower than the lowest floor!")
        elif floor_target > self.highest_floor:
            print("Error! Your target floor is higher than the highest floor")
        else:
            print("You already are in the same floor!")

    def floor_up(self):
        self.current_floor += 1
        print(f"Up! Now in floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Down! Now in floor: {self.current_floor}")


class House:
    def __init__(self, lowest_floor, highest_floor, elevator_amount):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevator_amount = elevator_amount
        self.elevator_list = []

        for i in range(elevator_amount):
            elevator = Elevator(lowest_floor, highest_floor)
            self.elevator_list.append(elevator)

    def use_elevator(self, elevator_num, target_floor):
        if self.elevator_amount >= elevator_num > 0:
            print(f"Elevators in the house: {self.elevator_amount}. Using elevator {elevator_num}:")
            self.elevator_list[elevator_num - 1].move_to_floor(target_floor)
        else:
            print("Elevator number in use_elevator out of range of the elevator amount!\n")


hs = House(0, 10, 5)

hs.use_elevator(1, 5)
hs.use_elevator(2, 8)

hs.use_elevator(1, 3)
hs.use_elevator(2, 5)
