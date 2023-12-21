import re
from collections import deque


def load_codes() -> list[str]:
    with open('aoc_dec_21.txt') as f:
        lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    return lines


def parse_input(input_lines):
    return [[c for c in line] for line in input_lines]


def walk(input_grid):
    grid_visited = [[c for c in line] for line in input_grid]
    steps = [[100 for c in line] for line in input_grid]
    start = []
    visit_next = deque()
    for i, line in enumerate(input_grid):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
                grid_visited[i][j] = 'O'
                visit_next.append([start, 0])
                steps[i][j] = 0
    # while len(visit_next) > 0:
    #     node = visit_next.popleft()
    #     grid_visited[node[0][0]][node[0][1]] = '.'
    #     grid_visited, steps, visit_next = one_step_each_dir(node, input_grid, grid_visited, visit_next, steps)
    #     for line in steps:
    #         print(''.join(['#' if l > 20 else str(l) for l in line]))
    #     print('____________________________________')
    nodes = [start]
    for i in range(64):
        new_nodes = []
        for n in nodes:
            grid_visited[n[0]][n[1]] = '.'
            new_ones = one_step(n, input_grid)
            for new_n in new_ones:
                if new_n not in new_nodes:
                    new_nodes.append(new_n)
                    grid_visited[new_n[0]][new_n[1]] = 'O'
        nodes = new_nodes
        # for line in grid_visited:
        #    print(''.join(line))
        # print('____________________________________')
    return count_occupied_fields(grid_visited)


def count_occupied_fields(grid_visited) -> int:
    return sum([line.count('O') for line in grid_visited])


def one_step(node, input_grid):
    current_node = node
    to_visit = []
    if current_node[0] > 0 and input_grid[current_node[0] - 1][current_node[1]] != '#':
        to_visit.append((current_node[0] - 1, current_node[1]))
    if current_node[1] > 0 and input_grid[current_node[0]][current_node[1]-1] != '#':
        to_visit.append((current_node[0], current_node[1] - 1))
    if current_node[0] < len(input_grid)-1 and input_grid[current_node[0] + 1][current_node[1]] != '#':
        to_visit.append((current_node[0] + 1, current_node[1]))
    if current_node[1] < len(input_grid[0])-1 and input_grid[current_node[0]][current_node[1]+1] != '#':
        to_visit.append((current_node[0], current_node[1]+1))
    return to_visit


def one_step_each_dir(node, input_grid, grid_visited, to_visit, step_grid):
    # north, south, east, or west (in case it is not blocked, and it is not already visited)
    current_node = node[0]
    steps = node[1] + 1
    if current_node[0] > 0 and input_grid[current_node[0] - 1][current_node[1]] != '#':
        if grid_visited[current_node[0] - 1][current_node[1]] == 'O':
            if step_grid[current_node[0] - 1][current_node[1]] > steps:
                to_visit.append([(current_node[0] - 1, current_node[1]), steps])
                step_grid[current_node[0] - 1][current_node[1]] = steps
        else:
            to_visit.append([(current_node[0] - 1, current_node[1]), steps])
            grid_visited[current_node[0] - 1][current_node[1]] = 'O'
            step_grid[current_node[0] - 1][current_node[1]] = steps
    if current_node[1] > 0 and input_grid[current_node[0]][current_node[1]-1] != '#':
        if grid_visited[current_node[0]][current_node[1]-1] == 'O':
            if step_grid[current_node[0]][current_node[1]-1] > steps:
                to_visit.append([(current_node[0], current_node[1] - 1), steps])
                step_grid[current_node[0]][current_node[1] - 1] = steps
        else:
            grid_visited[current_node[0]][current_node[1]-1] = 'O'
            to_visit.append([(current_node[0], current_node[1]-1), steps])
            step_grid[current_node[0]][current_node[1] - 1] = steps
    if current_node[0] < len(input_grid)-1 and input_grid[current_node[0] + 1][current_node[1]] != '#':
        if grid_visited[current_node[0] + 1][current_node[1]] == 'O':
            if step_grid[current_node[0] + 1][current_node[1]] > steps:
                to_visit.append([(current_node[0] + 1, current_node[1]), steps])
                step_grid[current_node[0] + 1][current_node[1]] = steps
        else:
            grid_visited[current_node[0] + 1][current_node[1]] = 'O'
            to_visit.append([(current_node[0] + 1, current_node[1]), steps])
            step_grid[current_node[0] + 1][current_node[1]] = steps
    if current_node[1] < len(input_grid[0])-1 and input_grid[current_node[0]][current_node[1]+1] != '#':
        if grid_visited[current_node[0]][current_node[1]+1] == 'O':
            if step_grid[current_node[0]][current_node[1]+1] > steps:
                to_visit.append([(current_node[0], current_node[1] + 1), steps])
                step_grid[current_node[0]][current_node[1] + 1] = steps
        else:
            grid_visited[current_node[0]][current_node[1]+1] = 'O'
            to_visit.append([(current_node[0], current_node[1]+1), steps])
            step_grid[current_node[0]][current_node[1] + 1] = steps
    return grid_visited, step_grid, to_visit


if __name__ == '__main__':
    some_input_lines = load_codes()
    in_grid = parse_input(some_input_lines)
    # -- part 1 --
    print(f"part 1: {walk(in_grid)}")
    # -- part 2 --
    print(f"part 2 {0}")
    pass
