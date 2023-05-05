import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


def part1(input_str: list[str]) -> int:
    return sum([len(phrase_list) == len(set(phrase_list)) for phrase_list in [l.split() for l in input_str]])


def part2(input_str: list[str]) -> int:
    return sum([len(sorted_phrase_list) == len(set(sorted_phrase_list)) for sorted_phrase_list in
                [list(map(lambda phrase: "".join(sorted(phrase)), phrase_list)) for phrase_list in
                 [joined_phrases.split() for joined_phrases in input_str]]])



if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
