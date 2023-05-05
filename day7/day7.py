import sys
import re
from typing import Any

sys.path.append('../aochelpers.py')
from aochelpers import *


def part1(input_str: list[str]) -> str:
    # get programs, weights, and
    towers = {}
    for line in input_str:
        programs = re.findall(r"[a-z]+", line)
        weight = re.findall(r"\d+", line)
        towers[programs[0]] = (int(weight[0]), programs[1:])

    all_program_names = set(towers.keys())
    reference_program_names = set([k for p in towers.values() for k in p[1]])
    return list(all_program_names.difference(reference_program_names))[0]

def sum_tree(start_tower, towers):
    weight = towers[start_tower][0] + sum([sum_tree(tower, towers) for tower in towers[start_tower][1]])
    return weight


def count(lst: list) -> dict:
    # counts how many of something there are in a list
    out = {}
    for item in lst:
        if item in out:
            out[item] +=1
        else:
            out[item] = 1
    return out


def odd_one_out(lst: list[Any]) -> Any:
    counts = count(lst)
    if len(set(lst)) != 1:
        odd = min(counts, key=lambda x: counts[x])
    else:
        return None
    return odd


def part2(input_str: list[str]) -> int:
    towers = {}
    for line in input_str:
        programs = re.findall(r"[a-z]+", line)
        weight = re.findall(r"\d+", line)
        towers[programs[0]] = (int(weight[0]), programs[1:])

    # call part1 to get the starting tower
    current_tower = part1(input_str)
    last_tower = None
    while True:
        next_towers = towers[current_tower][1]
        weights = [sum_tree(tower, towers) for tower in towers[current_tower][1]]
        weights_and_towers = dict(zip(weights, next_towers))
        odd_weight_out = odd_one_out(weights)

        if odd_weight_out is not None:
            next_tower = weights_and_towers[odd_weight_out]
            last_tower = current_tower
            current_tower = next_tower
        else:
            break
    in_balanced_tower = last_tower
    weights = [sum_tree(tower, towers) for tower in towers[in_balanced_tower][1]]
    counted_weights = count(weights)
    target_weight = max(counted_weights, key=lambda x: counted_weights[x])
    current_weight = sum_tree(current_tower, towers)
    return towers[current_tower][0] - (current_weight - target_weight)


if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
