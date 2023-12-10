
def load_codes() -> list[str]:
    with open('aoc_dec_10.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_input_into_matrix(input_lines: list[str]) -> list[list[str]]:
    return [[c for c in line] for line in input_lines]


# #################################################
# #################### PART 1 #####################
# #################################################
def longest_path(input_matrix: list[list[str]]) -> int:
    """calculate the highest distance of the starting point 'S' """
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
                    directions.append([1, 0])  # down
                if input_matrix[line_idx][pos - 1] == 'L' or input_matrix[line_idx][pos - 1] == 'F' or \
                        input_matrix[line_idx][pos - 1] == '-':
                    directions.append([0, -1])  # left
                if input_matrix[line_idx][pos + 1] == '7' or input_matrix[line_idx][pos + 1] == 'J' or \
                        input_matrix[line_idx][pos + 1] == '-':
                    directions.append([0, 1])  # right
    current_positions = [start_position for i in range(2)]
    steps = [0 for i in range(2)]
    while not (current_positions[0][0] == current_positions[1][0] and current_positions[0][1] == current_positions[1][
        1] and steps[0] != 0):
        for dir_idx in range(2):
            steps[dir_idx] += 1
            current_label = input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][
                current_positions[dir_idx][1] + directions[dir_idx][1]]
            input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][
                current_positions[dir_idx][1] + directions[dir_idx][1]] = str(steps[dir_idx])
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

    return steps[0]


# #################################################
# #################### PART 2 #####################
# #################################################
def inside_loop(input_matrix: list[list[str]]) -> int:
    """Attention: this is a very long and dirty funtion
    Its goal is to fill the inside (or outside) of a cycle"""
    original_grid = [[c for c in line] for line in input_matrix]
    # calculate starting position and starting directions
    for line_idx in range(len(input_matrix)):
        for pos in range(len(input_matrix[line_idx])):
            if input_matrix[line_idx][pos] == 'S':
                # replace with distance label
                input_matrix[line_idx][pos] = '#'
                start_position = [line_idx, pos]
                directions = []
                if input_matrix[line_idx - 1][pos] == '|' or input_matrix[line_idx - 1][pos] == 'F' or \
                        input_matrix[line_idx - 1][pos] == '7':
                    directions.append([-1, 0])  # up
                if input_matrix[line_idx + 1][pos] == '|' or input_matrix[line_idx + 1][pos] == 'J' or \
                        input_matrix[line_idx + 1][pos] == 'L':
                    directions.append([1, 0])  # down
                if input_matrix[line_idx][pos - 1] == 'L' or input_matrix[line_idx][pos - 1] == 'F' or \
                        input_matrix[line_idx][pos - 1] == '-':
                    directions.append([0, -1])  # left
                if input_matrix[line_idx][pos + 1] == '7' or input_matrix[line_idx][pos + 1] == 'J' or \
                        input_matrix[line_idx][pos + 1] == '-':
                    directions.append([0, 1])  # right
    # follow a path and mark tiles that corresponds to the main cycle as '#',
    # this is important to filter the other tiles out later on
    tmp_dirs = [d for d in directions]      # don't forget the starting direction!
    current_positions = [start_position for i in range(2)]
    steps = [0 for i in range(2)]
    while not (current_positions[0][0] == current_positions[1][0] and current_positions[0][1] == current_positions[1][
        1] and steps[0] != 0):
        for dir_idx in range(2):
            steps[dir_idx] += 1
            current_label = input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][
                current_positions[dir_idx][1] + directions[dir_idx][1]]
            input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][
                current_positions[dir_idx][1] + directions[dir_idx][1]] = '#'
            current_positions[dir_idx] = [current_positions[dir_idx][0] + directions[dir_idx][0],
                                          current_positions[dir_idx][1] + directions[dir_idx][1]]
            # get new direction for each tile that might occur
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
    # filter all tiles that are not part of the main cycle and replace them with '.'
    for line_idx in range(len(input_matrix)):
        for pos in range(len(input_matrix[line_idx])):
            if input_matrix[line_idx][pos] != '#':
                original_grid[line_idx][pos] = '.'
    input_matrix = original_grid
    # filling
    directions = tmp_dirs
    current_positions = [start_position for i in range(2)]
    steps = [0 for i in range(2)]
    tiles = ['|', '-', 'L', 'F', '7', 'S', 'J']     # path tiles, don't mark them with '#'
    s = [s for s in start_position]
    while not (current_positions[0][0] == s[0] and current_positions[0][1] == s[1] and steps[0] != 0):
        dir_idx = 0
        steps[dir_idx] += 1
        current_label = input_matrix[current_positions[dir_idx][0] + directions[dir_idx][0]][
            current_positions[dir_idx][1] + directions[dir_idx][1]]
        current_positions[dir_idx] = [current_positions[dir_idx][0] + directions[dir_idx][0],
                                      current_positions[dir_idx][1] + directions[dir_idx][1]]
        # While walking along the previously calculated path, always look at same side of the current tile.
        # Doing this, these tiles same side next to the current is always inside the loop.
        # To get all tiles outside the loop, simply hang a 'not' before the direction checks.
        if current_label == '|':
            if directions[dir_idx][0] != 1:
                # going up
                if input_matrix[current_positions[dir_idx][0]][
                                current_positions[dir_idx][1] - 1] not in tiles:
                    # left-hand side
                    input_matrix[current_positions[dir_idx][0]][
                                 current_positions[dir_idx][1] - 1] = '#'
            else:
                # going down
                if input_matrix[current_positions[dir_idx][0]][
                                current_positions[dir_idx][1] + 1] not in tiles:
                    # left-hand side
                    input_matrix[current_positions[dir_idx][0]][
                                 current_positions[dir_idx][1] + 1] = '#'
            directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 1 else [-1, 0]
        if current_label == '-':
            if directions[dir_idx][1] != -1:
                # going left
                if input_matrix[current_positions[dir_idx][0] - 1][
                                current_positions[dir_idx][1]] not in tiles:
                    input_matrix[current_positions[dir_idx][0] - 1][
                                 current_positions[dir_idx][1]] = '#'
            else:
                # going right
                if input_matrix[current_positions[dir_idx][0] + 1][
                                current_positions[dir_idx][1]] not in tiles:
                    input_matrix[current_positions[dir_idx][0] + 1][
                                 current_positions[dir_idx][1]] = '#'
            directions[dir_idx] = [0, -1] if directions[dir_idx][1] == -1 else [0, 1]
        if current_label == 'J':
            if directions[dir_idx][0] != 0:
                # going down
                if input_matrix[current_positions[dir_idx][0] + 1][
                                current_positions[dir_idx][1]] not in tiles:
                    input_matrix[current_positions[dir_idx][0] + 1][
                                 current_positions[dir_idx][1]] = '#'
                if input_matrix[current_positions[dir_idx][0]][
                                current_positions[dir_idx][1] + 1] not in tiles:
                    input_matrix[current_positions[dir_idx][0]][
                                 current_positions[dir_idx][1] + 1] = '#'
            directions[dir_idx] = [-1, 0] if directions[dir_idx][0] == 0 else [0, -1]
        if current_label == 'L':
            if directions[dir_idx][0] == 0:
                # going left
                if input_matrix[current_positions[dir_idx][0] + 1][
                                current_positions[dir_idx][1]] not in tiles:
                    input_matrix[current_positions[dir_idx][0] + 1][
                                 current_positions[dir_idx][1]] = '#'
                if input_matrix[current_positions[dir_idx][0]][
                                current_positions[dir_idx][1] - 1] not in tiles:
                    input_matrix[current_positions[dir_idx][0]][
                                 current_positions[dir_idx][1] - 1] = '#'
            directions[dir_idx] = [-1, 0] if directions[dir_idx][0] == 0 else [0, 1]
        if current_label == 'F':
            if directions[dir_idx][0] != 0:
                # going up
                if input_matrix[current_positions[dir_idx][0] - 1][
                                current_positions[dir_idx][1]] not in tiles:
                    input_matrix[current_positions[dir_idx][0] - 1][
                                 current_positions[dir_idx][1]] = '#'
                if input_matrix[current_positions[dir_idx][0]][
                                current_positions[dir_idx][1] - 1] not in tiles:
                    input_matrix[current_positions[dir_idx][0]][
                                 current_positions[dir_idx][1] - 1] = '#'
            directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 0 else [0, 1]
        if current_label == '7':
            if directions[dir_idx][0] == 0:
                # going right
                if input_matrix[current_positions[dir_idx][0] - 1][
                                current_positions[dir_idx][1]] not in tiles:
                    input_matrix[current_positions[dir_idx][0] - 1][
                                 current_positions[dir_idx][1]] = '#'
                if input_matrix[current_positions[dir_idx][0]][
                                current_positions[dir_idx][1] + 1] not in tiles:
                    input_matrix[current_positions[dir_idx][0]][
                                 current_positions[dir_idx][1] + 1] = '#'
            directions[dir_idx] = [1, 0] if directions[dir_idx][0] == 0 else [0, -1]
    # mark neighbors of '#' as '#'
    for line_idx in range(1, len(input_matrix) - 1):
        for pos in range(1, len(input_matrix[line_idx]) - 1):
            if input_matrix[line_idx-1][pos] == '#' or input_matrix[line_idx+1][pos] == '#' or\
               input_matrix[line_idx][pos-1] == '#' or input_matrix[line_idx][pos+1] == '#':
                if input_matrix[line_idx][pos] not in tiles:
                    input_matrix[line_idx][pos] = '#'
    # same thing backwards to cover all neighbors
    for line_idx in range(len(input_matrix) - 2, 0, -1):
        for pos in range(len(input_matrix[line_idx]) - 2, 0, -1):
            if input_matrix[line_idx-1][pos] == '#' or input_matrix[line_idx+1][pos] == '#' or\
               input_matrix[line_idx][pos-1] == '#' or input_matrix[line_idx][pos+1] == '#':
                if input_matrix[line_idx][pos] not in tiles:
                    input_matrix[line_idx][pos] = '#'

    for l in input_matrix:
        line = ''.join(l)
        print(line)
    # counting
    counter = 0
    for l in input_matrix:
        for c in l:
            if c == '#':
                counter += 1

    return counter


if __name__ == '__main__':
    some_input_lines = load_codes()
    # -- part 1 --
    print(longest_path(input_matrix=parse_input_into_matrix(input_lines=some_input_lines)))
    # -- part 2 --
    print(inside_loop(input_matrix=parse_input_into_matrix(input_lines=some_input_lines)))
    pass
