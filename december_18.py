import re
import time

import numpy as np
import itertools
import os
import random


def load_codes() -> list[str]:
    with open('aoc_dec_18.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_input(input_lines: list[str]) -> list[tuple[str, int, str]]:
    sequence = []
    for line in input_lines:
        dis = re.findall(r'\d+', line)[0]
        dir = re.findall(r'D|U|R|L', line)[0]
        color = re.findall(r'#[0-9a-f]+', line)[0].replace('#', '')
        sequence.append((dir, int(dis), color))
    return sequence


def extend_field(grid: list[list[str]], direction: str = 'R', amount: int = 1) -> list[list[str]]:
    if direction == 'R':
        for a in range(amount):
            for row in range(len(grid)):
                grid[row].append('.')
    elif direction == 'L':
        for a in range(amount):
            for row in range(len(grid)):
                grid[row].insert(0, '.')
    elif direction == 'U':
        for a in range(amount):
            grid.insert(0, ['.' for i in grid[0]])
    elif direction == 'D':
        for a in range(amount):
            grid.append(['.' for i in grid[0]])
    return grid


def create_plan(sequence: list[tuple[str, int, str]]) -> list[[list[str]]]:
    in_grid = [['.' for _ in range(10)] for k in range(10)]
    current_pos = [0, 0]
    for direction, distance, color in sequence:
        if direction == 'U':
            if current_pos[0] - distance < 0:
                # after extending need to calculate the new current position
                in_grid = extend_field(in_grid, direction='U', amount=distance)
                current_pos[0] = current_pos[0] + distance
            # walk and mark fields, then adjust current position
            for i in range(distance):
                current_pos[0] -= 1
                in_grid[current_pos[0]][current_pos[1]] = '#'
        elif direction == 'D':
            if current_pos[0] + distance > len(in_grid) - 1:
                # after extending need to calculate the new current position
                in_grid = extend_field(in_grid, direction='D', amount=distance)
            # walk and mark fields, then adjust current position
            for i in range(distance):
                current_pos[0] += 1
                in_grid[current_pos[0]][current_pos[1]] = '#'
        elif direction == 'L':
            if current_pos[1] - distance < 0:
                # after extending need to calculate the new current position
                in_grid = extend_field(in_grid, direction='L', amount=distance)
                current_pos[1] = current_pos[1] + distance
            # walk and mark fields, then adjust current position
            for i in range(distance):
                current_pos[1] -= 1
                in_grid[current_pos[0]][current_pos[1]] = '#'
        elif direction == 'R':
            if current_pos[1] + distance > len(in_grid[0]) - 1:
                # after extending need to calculate the new current position
                in_grid = extend_field(in_grid, direction='R', amount=distance)
            # walk and mark fields, then adjust current position
            for i in range(distance):
                current_pos[1] += 1
                in_grid[current_pos[0]][current_pos[1]] = '#'

        #show_grid(in_grid)

    return in_grid


def flood_fill(x, y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return
    # secondly, check if the current position equals the old value
    if grid[y][x] != old:
        return

    # thirdly, set the current position to the new value
    grid[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new)
    flood_fill(x-1, y, old, new)
    flood_fill(x, y+1, old, new)
    flood_fill(x, y-1, old, new)




def fill_insides(grid):
    grid = extend_field(grid, direction='L', amount=1)
    new_grid = [[c for c in line] for line in grid]
    # inside outside method
    for i, line in enumerate(grid):
        pass

    return new_grid


def count_filled_fields(grid):
    return sum([line.count('#') + line.count('*') for line in grid])


def show_grid(grid):
    print('\n' * 100)
    # os.system('cls')
    for line in grid:
        print(''.join(line))


import sys
sys.setrecursionlimit(500)
some_input_lines = load_codes()
in_seq = parse_input(input_lines=some_input_lines)
grid = create_plan(sequence=in_seq)
flood_fill(x=1, y=1, old='.', new='*')
show_grid(grid)


if __name__ == '__main__':
    end_time = time.time() + 100

    while time.time() > end_time:
        pass
    # extend_field(grid=in_grid, direction='U', amount=1)
    # -- part 1 --
    print(f"part 1: {count_filled_fields(grid=grid)}")
    # -- part 2 --
    print(f"part 2 {0}")
    pass
