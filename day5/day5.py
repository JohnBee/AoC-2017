import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


def part1(input_str: list[str]) -> int:
    jumps = list(map(int, input_str))
    pos = 0
    total_steps = 0
    while pos < len(jumps):
        next_pos = pos + jumps[pos]
        jumps[pos] += 1
        pos = next_pos
        total_steps += 1
    return total_steps



def part2(input_str: list[str]) -> int:
    jumps = list(map(int, input_str))
    pos = 0
    total_steps = 0
    while pos < len(jumps):
        next_pos = pos + jumps[pos]
        if jumps[pos] >= 3:
            jumps[pos] -= 1
        else:
            jumps[pos] += 1
        pos = next_pos
        total_steps += 1
    return total_steps


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
