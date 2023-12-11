import re
import itertools


def load_codes() -> list[str]:
    with open('aoc_dec_11.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


# #################################################
# #################### PART 1 #####################
# #################################################
def parse_input_p1(input_lines: list[str]) -> list[list[str]]:
    # take horizontal and vertical expansion into account
    mutated_lines = [l for l in input_lines]
    for i in range(len(input_lines)-1, -1, -1):
        if len(re.findall(r'\.+', input_lines[i])[0]) == len(input_lines[i]):
            # a line full of '.' -> insert another line full of '.'
            mutated_lines.insert(i, ''.join(['.' for j in range(len(input_lines[i]))]))
    another_grid = [l for l in mutated_lines]
    for i in range(len(mutated_lines[0])-1, -1, -1):
        curr = ''.join([mutated_lines[k][i] for k in range(len(mutated_lines))])
        if len(re.findall(r'\.+', curr)[0]) == len(mutated_lines):
            for j in range(len(mutated_lines)):
                another_grid[j] = another_grid[j][:i] + '.' + another_grid[j][i:]

    # converto into grid
    grid = [[c for c in line] for line in another_grid]

    return grid


def shortest_path_p1(grid: list[list[str]]) -> int:
    """first calc manhattan distance between two points."""
    # label '#'
    count = 1
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                grid[i][j] = str(count)
                positions.append([i, j])
                count += 1
    combinations = int(count * (count-1) / 2)
    pairs = [i for i in itertools.combinations(list(range(1, count)), r=2)]
    distances = []
    for a, b in pairs:
        # calc manhattan distance between a and b here (row dist + col dist)
        distances.append(abs(positions[a-1][0] - positions[b-1][0]) + abs(positions[a-1][1] - positions[b-1][1]))

    return sum(distances)


# #################################################
# #################### PART 2 #####################
# #################################################
def parse_input_p2(input_lines: list[str]) -> tuple[list[list[str]], list[int], list[int]]:
    # take horizontal and vertical expansion into account
    mutated_lines = [l for l in input_lines]
    lines_w_plus = []
    for i in range(len(input_lines)-1, -1, -1):
        if len(re.findall(r'\.+', input_lines[i])[0]) == len(input_lines[i]):
            # a line full of '.' -> insert another line full of '.'
            mutated_lines[i] = ''.join(['+' for j in range(len(input_lines[i]))])
            lines_w_plus.append(i)
    cols_w_plus = []
    for i in range(len(input_lines[0])-1, -1, -1):
        curr = ''.join([input_lines[k][i] for k in range(len(input_lines))])
        if len(re.findall(r'\.+', curr)[0]) == len(input_lines):
            cols_w_plus.append(i)
            for j in range(len(input_lines)):
                mutated_lines[j] = mutated_lines[j][:i] + '+' + mutated_lines[j][1+i:]

    # converto into grid
    grid = [[c for c in line] for line in mutated_lines]

    return grid, lines_w_plus, cols_w_plus


def shortest_path_p2(grid: list[list[str]], rows: list[int], cols: list[int]) -> int:
    """first calc manhattan distance between two points."""
    # label '#'
    count = 1
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                grid[i][j] = str(count)
                positions.append([i, j])
                count += 1
    combinations = int(count * (count-1) / 2)       # to check: this is the number of possible combinations of pairs
    pairs = [i for i in itertools.combinations(list(range(1, count)), r=2)]
    distances = []
    for a, b in pairs:
        # calc manhattan distance between a and b here (row dist + col dist)
        # check if '+' on the path
        addon = 0
        insides = []
        for r in rows:
            if positions[a-1][0] <= r <= positions[b-1][0] or positions[b-1][0] <= r <= positions[a-1][0]:
                addon += 1000000
                insides.append({'row': r})
        for c in cols:
            if positions[a-1][1] <= c <= positions[b-1][1] or positions[b-1][1] <= c <= positions[a-1][1]:
                addon += 1000000
                insides.append({'col': c})
        distances.append(abs(positions[a-1][0] - positions[b-1][0]) + abs(positions[a-1][1] - positions[b-1][1]) + addon - len(insides))

    return sum(distances)


if __name__ == '__main__':
    some_input_lines = load_codes()
    # -- part 1 --
    input_grid = parse_input_p1(input_lines=some_input_lines)
    for row in input_grid:
        print(''.join(row))
    print(shortest_path_p1(grid=input_grid))
    # -- part 2 --
    input_grid, rows_plus, cols_plus = parse_input_p2(input_lines=some_input_lines)
    print(shortest_path_p2(grid=input_grid, rows=rows_plus, cols=cols_plus))
    pass
