import re


def load_codes() -> list[str]:
    with open('aoc_dec_09.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_lines(input_lines: list[str]) -> list[list[int]]:
    return [[int(s) for s in re.findall(r'-\d+|\d+', input_line)] for input_line in input_lines]


def calc_levels(line: list[int]) -> list[list[int]]:
    l_idx = 0
    levels = []
    current_line = line
    levels.append(current_line)
    while not all(l == 0 for l in levels[l_idx]):
        current_line = [j - i for i, j in zip(current_line[:-1], current_line[1:])]
        levels.append(current_line)
        l_idx += 1
    return levels


# #################################################
# #################### PART 1 #####################
# #################################################
def calc_next_value(input_lines: list[str]) -> int:
    lines = parse_lines(input_lines)
    values_collection = []
    for line in lines:
        levels = calc_levels(line)
        # calculate next value bottom up
        i = len(levels) - 2
        while i >= 0:
            levels[i].append(levels[i+1][-1] + levels[i][-1])
            i -= 1
        values_collection.append(levels[0][-1])

    return sum(values_collection)


# #################################################
# #################### PART 2 #####################
# #################################################
def calc_previous_value(input_lines: list[str]) -> int:
    lines = parse_lines(input_lines)
    values_collection = []
    for line in lines:
        levels = calc_levels(line)
        # calculate next value bottom up
        i = len(levels) - 2
        while i >= 0:
            levels[i].insert(0, levels[i][0] - levels[i+1][0])
            i -= 1
        values_collection.append(levels[0][0])

    return sum(values_collection)


if __name__ == '__main__':
    input_lines = load_codes()

    # --part 1 --
    print(calc_next_value(input_lines))
    # -- part 2 --
    print(calc_previous_value(input_lines))
    pass