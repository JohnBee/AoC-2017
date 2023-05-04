import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


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


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
