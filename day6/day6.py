import sys
from typing import Any

sys.path.append('../aochelpers.py')
from aochelpers import *


def to_state(_d: dict) -> list[tuple[Any, Any]]:
    return [(k, _d[k]) for k in _d]


def part1(input_str: list[str]) -> int:
    banks = dict(enumerate(map(int, input_str[0].split())))
    states = []
    cycles = 0
    while to_state(banks) not in states:
        states.append(to_state(banks))

        # get bank with most
        largest_index = max(banks, key=lambda k: banks[k])
        largest_value = banks[largest_index]

        # distribute amongst other banks
        banks[largest_index] = 0
        for index in range(largest_index + 1, largest_index + len(banks)):
            i = index % len(banks)
            if largest_value == 0:
                break
            banks[i] += 1
            largest_value -= 1
        cycles += 1

    return cycles


def part2(input_str: list[str]) -> int:
    banks = dict(enumerate(map(int, input_str[0].split())))
    for i in range(2):
        states = []
        cycles = 0
        while to_state(banks) not in states:
            states.append(to_state(banks))

            # get bank with most
            largest_index = max(banks, key=lambda k: banks[k])
            largest_value = banks[largest_index]

            # distribute amongst other banks
            banks[largest_index] = 0
            for index in range(largest_index + 1, largest_index + len(banks)):
                i = index % len(banks)
                if largest_value == 0:
                    break
                banks[i] += 1
                largest_value -= 1
            cycles += 1

    return cycles


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
