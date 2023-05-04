def part1(input_str: list[str]) -> int:
    pass


def part2(input_str: list[str]) -> int:
    pass


def load_file(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
    return lines


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
