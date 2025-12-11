# split line into list of ranges
# for number range, scan for number that are composed of two identical numbers
# e.g. 1-12 = 11, 1009-1011 = 1010, 11-22 = 11 + 22
# sum all duplicated numbers
# return result


def main() -> int:
    with open("input/day-2.txt", "r") as f:
        line = f.read().split(",")
    parsed_input = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in line]

    result = 0
    for start, end in parsed_input:
        for i in range(start, end + 1):
            result += calculate_silly_number(i)
    return result


def calculate_silly_number(number: int) -> int:
    code = str(number)
    possibles_subcode_indices = [
        (x, len(code) // x)
        for x in range(1, (len(code) // 2) + 1)
        if len(code) % x == 0
    ]

    for size, n in possibles_subcode_indices:
        sub_codes = [code[step * size : (step + 1) * size] for step in range(n)]
        if len(set(sub_codes)) == 1:
            print(f"Found sub code {sub_codes[1]} {n} times in code {code}!")
            return number
    return 0


if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")
