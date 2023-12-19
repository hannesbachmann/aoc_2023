import re
import numpy as np
import itertools


def load_codes() -> list[str]:
    with open('test_02.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def beams_p1(input_lines) -> int:
    energized_map = [['.' for i in l] for l in input_lines]
    start_positions = [0, 0]
    e_map = move_p1(start_positions, [0, 1], input_lines)
    return 0


def move_p1(position, direction, input_lines):
    energized_map = [['.' for i in l] for l in input_lines]
    next_tile = [position[0] + direction[0], position[1] + direction[1]]
    while 1:
        if next_tile[0] < 0 or next_tile[0] >= len(input_lines) or next_tile[1] < 0 or next_tile[1] >= len(input_lines[0]):
            return energized_map
        else:
            # calc next position
            # 5 cases: - | / \ .
            # cases - and | split, recursion
            # cases / \
            # case . do forward
            pass




if __name__ == '__main__':
    some_input_lines = load_codes()
    pass
