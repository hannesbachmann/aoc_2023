import string
from math import lcm
import re


def load_codes() -> list[str]:
    with open('aoc_dec_10.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_input_into_matrix(input_lines: list[str]) -> list[list[str]]:
    return [[c for c in line] for line in input_lines]


def longest_path(input_matrix: list[list[str]]) -> int:
    # calculate starting position and starting directions
    for line_idx in range(len(input_matrix)):
        for pos in range(len(input_matrix[line_idx])):
            if input_matrix[line_idx][pos] == 'S':
                # replace with distance label
                input_matrix[line_idx][pos] = '0'
                start_position = [line_idx, pos]
                directions = []
                if input_matrix[line_idx - 1][pos] == '|' or input_matrix[line_idx - 1][pos] == 'F' or \
                        input_matrix[line_idx - 1][pos] == '7':
                    directions.append([-1, 0])  # up
                if input_matrix[line_idx + 1][pos] == '|' or input_matrix[line_idx + 1][pos] == 'J' or \
                        input_matrix[line_idx + 1][pos] == 'L':
                    directions.append([1, 0])   # down
                if input_matrix[line_idx][pos - 1] == 'L' or input_matrix[line_idx][pos - 1] == 'F' or \
                        input_matrix[line_idx][pos - 1] == '-':
                    directions.append([0, -1])  # left
                if input_matrix[line_idx][pos + 1] == '7' or input_matrix[line_idx][pos + 1] == 'J' or \
                        input_matrix[line_idx][pos + 1] == '-':
                    directions.append([0, 1])   # right
    current_positions = [start_position for i in range(2)]
    steps = [0 for i in range(2)]
    while not (current_positions[0][0] == current_positions[1][0] and current_positions[0][1] == current_positions[1][1] and steps[0] != 0):
        for dir_idx in range(2):
            steps[dir_idx] += 1
            current_label = input_matrix[current_positions[dir_idx][0]+directions[dir_idx][0]][current_positions[dir_idx][1]+directions[dir_idx][1]]
            input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][current_positions[dir_idx][1] + directions[dir_idx][1]] = str(steps[dir_idx])
            current_positions[dir_idx] = [current_positions[dir_idx][0] + directions[dir_idx][0],
                                          current_positions[dir_idx][1] + directions[dir_idx][1]]
            if current_label == '|':
                directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 1 else [-1, 0]
            if current_label == '-':
                directions[dir_idx] = [0, -1] if directions[dir_idx][1] == -1 else [0, 1]
            if current_label == 'J':
                directions[dir_idx] = [-1, 0] if directions[dir_idx][0] == 0 else [0, -1]
            if current_label == 'L':
                directions[dir_idx] = [-1, 0] if directions[dir_idx][0] == 0 else [0, 1]
            if current_label == 'F':
                directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 0 else [0, 1]
            if current_label == '7':
                directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 0 else [0, -1]
            print('')
    print(steps[0])

    return 0


def inside_loop(input_matrix: list[list[str]]) -> int:
    # calculate starting position and starting directions
    for line_idx in range(len(input_matrix)):
        for pos in range(len(input_matrix[line_idx])):
            if input_matrix[line_idx][pos] == 'S':
                # replace with distance label
                input_matrix[line_idx][pos] = '0'
                start_position = [line_idx, pos]
                directions = []
                if input_matrix[line_idx - 1][pos] == '|' or input_matrix[line_idx - 1][pos] == 'F' or \
                        input_matrix[line_idx - 1][pos] == '7':
                    directions.append([-1, 0])  # up
                if input_matrix[line_idx + 1][pos] == '|' or input_matrix[line_idx + 1][pos] == 'J' or \
                        input_matrix[line_idx + 1][pos] == 'L':
                    directions.append([1, 0])   # down
                if input_matrix[line_idx][pos - 1] == 'L' or input_matrix[line_idx][pos - 1] == 'F' or \
                        input_matrix[line_idx][pos - 1] == '-':
                    directions.append([0, -1])  # left
                if input_matrix[line_idx][pos + 1] == '7' or input_matrix[line_idx][pos + 1] == 'J' or \
                        input_matrix[line_idx][pos + 1] == '-':
                    directions.append([0, 1])   # right
    current_positions = [start_position for i in range(2)]
    steps = [0 for i in range(2)]
    while not (current_positions[0][0] == current_positions[1][0] and current_positions[0][1] == current_positions[1][1] and steps[0] != 0):
        for dir_idx in range(2):
            steps[dir_idx] += 1
            current_label = input_matrix[current_positions[dir_idx][0]+directions[dir_idx][0]][current_positions[dir_idx][1]+directions[dir_idx][1]]
            input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][current_positions[dir_idx][1] + directions[dir_idx][1]] = str(steps[dir_idx])
            current_positions[dir_idx] = [current_positions[dir_idx][0] + directions[dir_idx][0],
                                          current_positions[dir_idx][1] + directions[dir_idx][1]]
            if current_label == '|':
                directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 1 else [-1, 0]
            if current_label == '-':
                directions[dir_idx] = [0, -1] if directions[dir_idx][1] == -1 else [0, 1]
            if current_label == 'J':
                directions[dir_idx] = [-1, 0] if directions[dir_idx][0] == 0 else [0, -1]
            if current_label == 'L':
                directions[dir_idx] = [-1, 0] if directions[dir_idx][0] == 0 else [0, 1]
            if current_label == 'F':
                directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 0 else [0, 1]
            if current_label == '7':
                directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 0 else [0, -1]
    for line_idx in range(len(input_matrix)):
        for pos in range(len(input_matrix[line_idx])):
            p = re.compile(r'\d+')
            if p.match(input_matrix[line_idx][pos]):
                input_matrix[line_idx][pos] = '#'
            else:
                input_matrix[line_idx][pos] = '.'

    return 0


if __name__ == '__main__':
    input_lines = load_codes()
    input_grid = parse_input_into_matrix(input_lines=input_lines)
    # -- part 1 --
    # max_distance = longest_path(input_matrix=input_grid)
    # -- part 2 --
    n = inside_loop(input_matrix=input_grid)
    pass
