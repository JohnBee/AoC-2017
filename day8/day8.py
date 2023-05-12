import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


class Registers:
    def __init__(self):
        self.reg = {}
        self.highest_value = 0

    def __getitem__(self, item):
        if item in self.reg:
            return self.reg[item]
        else:
            self.reg[item] = 0
            return self.reg[item]

    def __setitem__(self, key, value):
        if value > self.highest_value:
            self.highest_value = value
        self.reg[key] = value


def run_program(input_str: list[str]) -> Registers:
    regs = Registers()
    operators = {">": lambda x, y: x > y,
                 ">=": lambda x, y: x >= y,
                 "==": lambda x, y: x == y,
                 "<": lambda x, y: x < y,
                 "<=": lambda x, y: x <= y,
                 "!=": lambda x, y: x != y}

    modifier = {"inc": lambda x: x,
                "dec": lambda x: -x}

    for cmd_str in input_str:
        tokens = cmd_str.split()
        reg = tokens[0]  # a
        op = tokens[1]  # inc dec
        val_op = int(tokens[2])  # +20, -20
        test_reg = tokens[4]  # b
        check_bool = tokens[5]
        check_val = int(tokens[6])

        if operators[check_bool](regs[test_reg], check_val):
            regs[reg] += modifier[op](val_op)
    return regs


def part1(input_str: list[str]) -> int:
    regs = run_program(input_str)
    return max(regs.reg.values())


def part2(input_str: list[str]) -> int:
    regs = run_program(input_str)
    return regs.highest_value


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
