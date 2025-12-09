# Dial from [0 - 99]
# Starts at 50
# Count the number of times dial hits 0


class Dial:
    def __init__(
        self,
        input_file: str,
        start_number: int = 50,
        min_number: int = 0,
        max_number: int = 99,
        click_number: int = 0,
    ):
        self.input_file = input_file
        self.number = start_number
        self.n_clicks = 0
        self.min = min_number
        self.max = max_number
        self.click_number = click_number
        self.full_rotation = self.max + 1

    def turn(self, rotation: str):
        direction = 1 if rotation[0] == "R" else -1
        if (
            self.number == self.click_number and direction == -1
        ):  # Turning left from 0 results in an extra click
            self.n_clicks -= 1
        n_rotations = int(rotation[1:])

        while n_rotations > self.full_rotation:
            n_rotations -= self.full_rotation
            self.n_clicks += 1

        total_rotations = direction * n_rotations

        self.number += total_rotations

        if self.number == self.click_number:
            self.n_clicks += 1
        else:
            while self.number < self.min:
                self.number += self.full_rotation
                self.n_clicks += 1
            while self.number > self.max:
                self.number -= self.full_rotation
                self.n_clicks += 1

        # if self.number == self.click_number:
        #     self.n_clicks += 1

        # for i in range(0, n_rotations):
        #     self.number += direction
        #
        #     if self.number == self.click_number:
        #         print("BINGO")
        #         self.n_clicks += 1
        #
        #     if self.number > self.max:
        #         self.number = self.min
        #     if self.number < self.min:
        #         self.number = self.max

    def run_input(self) -> int:
        with open(self.input_file, "r") as f:
            for line in f:
                self.turn(line)
                print(f"Line: {line}")
                print(f"Dial: {self.number}, clicks: {self.n_clicks}")
        return self.n_clicks


if __name__ == "__main__":
    # dial = Dial("input/example-day-1.txt")
    dial = Dial("input/day-1.txt")
    password = dial.run_input()
    print(password)
