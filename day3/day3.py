import sys

sys.path.append('../aochelpers.py')
from aochelpers import *


def number_gen(initial_value: int):
    v = initial_value
    while True:
        yield v
        v += 1


def layer_size(layer: int) -> int:
    if layer == 0:
        return 0
    else:
        return layer * 8


def __final_layer_value(layer_number: int) -> int:
    if layer_number == 0:
        return 0
    if layer_number == 1:
        return 8
    return __final_layer_value(layer_number-1) + layer_size(layer_number)


def final_layer_value(layer_number: int) -> int:
    return __final_layer_value(layer_number)+1


def calculate_pos(target_value: int) -> (int, int):
    pos = [0, 0]
    # 0 > 8 > 16 > 24 > 32 > 40 > 48 >
    # 0 > 8 > 24 > 48 > 80 > 120 > 168
    # side length increases by 2 each time

    # calculate the layer the number is on
    current_layer = 0
    layer_value = final_layer_value(current_layer)
    while layer_value <= target_value:
        layer_value = final_layer_value(current_layer)
        current_layer += 1

    # step one back to get the ring/layer the value is on.
    current_layer -= 1

    # calculate the value that starts the layer
    last_layer_value = final_layer_value(current_layer)

    # how many values make us this layer
    last_layer_size = layer_size(current_layer)

    # the size of each of the 4 sides of the square layer
    side_length = last_layer_size // 4

    # calculate which side the target value is on, right, top, left, bottom
    temp = last_layer_value - last_layer_size
    dist = target_value - temp
    # walk counter-clockwise round
    # 0 right side, 1 top side, 2, left side, 3 bottom side
    side = dist // side_length

    pos = [current_layer, current_layer]  # bottom right corner

    # if bottom right corner is the value need to adjust as the algorithm overcompensates
    if dist == 0:
        return pos[0] - 1, pos[1] - 1  # bottom right corner logic


    # move the current value around the sides to start counting
    current_value = final_layer_value(current_layer - 1) + side_length * side

    # right side
    if side == 0:
        # pos stays same
        while current_value != target_value:
            current_value += 1
            pos = [pos[0], pos[1] - 1]  # walk up

    # top side
    if side == 1:
        pos = [pos[0], -pos[1]]  # reflect in y
        while current_value != target_value:
            current_value += 1
            pos = [pos[0] - 1, pos[1]]  # walk to left

    # left side
    if side == 2:
        pos = [-pos[0], -pos[1]]
        while current_value != target_value:
            current_value += 1
            pos = [pos[0], pos[1] + 1]  # walk down

    # bottom side
    if side == 3:
        pos = [-pos[0], pos[1]]
        while current_value != target_value:
            current_value += 1
            pos = [pos[0] + 1, pos[1]]  # walk right

    return pos[0], pos[1]


def part1(input_str: list[str]) -> int:
    target_value = int(input_str[0])
    # target_value = 25
    pos = calculate_pos(target_value)

    return abs(pos[0]) + abs(pos[1])


def part2(input_str: list[str]) -> int:
    target_value = int(input_str[0])
    spiral_map = {(0, 0): 1}
    last_value = 1
    step = 2
    while last_value < target_value:
        next_pos = calculate_pos(step)
        value = 0
        directions = [(next_pos[0] + x, next_pos[1] + y) for x in range(-1, 2) for y in range(-1, 2)]
        for dir_pos in directions:
            if dir_pos in spiral_map:
                value += spiral_map[dir_pos]
        spiral_map[next_pos] = value
        last_value = value
        step += 1
    return last_value



if __name__ == "__main__":
    lines = load_file("input")
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
