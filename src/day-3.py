# For every line in input, find the two digits that, when concatenated,
# produces the highest number
# e.g. 12345 = 45, 51115 = 55, 23409 = 49, 88889112 = 92
# Bonus:
# Take the twelve digits that produce the highest number


def main():
    with open("input/day-3.txt", "r") as f:
        total_joltage = 0
        for line in f.readlines():
            joltage = find_highest_joltage(line.strip())
            total_joltage += joltage
    print(f"Total joltage: {total_joltage}")


def find_highest_joltage(bank: str) -> int:
    joltages = []
    voltages = [int(x) for x in list(bank)]
    for i in range(12, 0, -1):  # looking for 12 digits
        jolt = _get_voltage_for_index(voltages, i)
        joltages.append(str(jolt))
        jolt_i = voltages.index(jolt)
        voltages = voltages[jolt_i + 1 :]

    joltage_string = "".join(joltages)
    return int(joltage_string)


def _get_voltage_for_index(voltages: list[int], digit: int) -> int:
    # Play room is the number of indices we can look into for the highest voltage
    play_room = (len(voltages) + 1) - digit
    if play_room == 1:
        return voltages[0]

    sorted_sub_voltages = sorted(voltages[:play_room], reverse=True)
    max_voltage = sorted_sub_voltages[0]
    return max_voltage


def _get_voltage_index_old(voltages: list[int], first: bool) -> tuple[int, int]:
    final_index = len(voltages) - 1
    sorted_voltages = sorted(voltages, reverse=True)
    max_volt = sorted_voltages[0]
    if (voltages.index(max_volt) == final_index) and first:
        max_volt = sorted_voltages[1]
    return max_volt, voltages.index(max_volt)


if __name__ == "__main__":
    main()
