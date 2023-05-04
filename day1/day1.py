def part1(input_str: list[str]) -> int:
    total = 0
    inStr = input_str[0]
    for index in range(len(inStr)):
        if inStr[index] == inStr[(index+1) % len(inStr)]:
            total += int(inStr[index])
    return total


def part2(input_str: list[str]) -> int:
    total = 0
    inStr = input_str[0]
    for index in range(len(inStr)):
        if inStr[index] == inStr[(index + len(inStr)//2) % len(inStr)]:
            total += int(inStr[index])
    return total


def load_file(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
