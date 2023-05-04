import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


def reformat(input_str: list[str]) -> list[list[int]]:
    return [list(map(int, line.split())) for line in input_str]


def evenly_divides(a: int, b: int) -> bool:
    return a % b == 0


def part1(input_str: list[str]) -> int:
    formatted_input = reformat(input_str)
    rows = len(formatted_input[0])
    columns = len(formatted_input)
    checksum = 0
    for row in formatted_input:
        smallest = min(row)
        biggest = max(row)
        checksum += biggest - smallest
    return checksum


def part2(input_str: list[str]) -> int:
    formatted_input = reformat(input_str)
    totals = []
    for row in formatted_input:
        for index1 in range(0, len(row)-1):
            for index2 in range(index1+1, len(row)):
                a = row[index1]
                b = row[index2]
                if evenly_divides(a, b):
                    totals.append(a // b)
                elif evenly_divides(b, a):
                    totals.append(b // a)
    return sum(totals)



if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
