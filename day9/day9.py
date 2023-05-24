import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


def build_groups(char_stream: list[chr]):
    def get_garbage(stream: list[chr]):
        garbage = ""
        c = None
        while c != ">":
            c = stream.pop()

            if c == "!":
                stream.pop()
            elif c == ">":
                return garbage
            elif c is not None:
                garbage += c

    groups = []
    while len(char_stream):
        c = char_stream.pop()
        if c == "{":
            groups.append(build_groups(char_stream))

        elif c == ",":
            pass

        elif c == "!":
            char_stream.pop()  # ignore next character

        elif c == "<":
            groups.append(get_garbage(char_stream))

        elif c == "}":
            return groups

        else:
            raise ValueError("Error Parsing.")

    return groups


def score_groups(groups: list, depth=0) -> int:
    c = 0
    if type(groups) == list:
        c = depth
        for group in groups:
            c += score_groups(group, depth+1)
    print(c)
    return c


def sum_garbage(groups: list):
    if type(groups) == list:
        return sum([sum_garbage(group) for group in groups])
    else:
        return len(groups)


def part1(input_str: list[str]) -> int:
    stream = list(input_str[0])
    stream.reverse()
    g = build_groups(stream)
    s = score_groups(g)
    return s


def part2(input_str: list[str]) -> int:
    stream = list(input_str[0])
    stream.reverse()
    g = build_groups(stream)
    return sum_garbage(g)



if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
