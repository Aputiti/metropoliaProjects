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


elev = Elevator(0, 8)

elev.move_to_floor(5)
elev.move_to_floor(0)
