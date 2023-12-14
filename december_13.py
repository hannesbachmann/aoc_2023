import re
import itertools


def load_codes() -> list[str]:
    with open('aoc_dec_13.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def split_patterns(input_lines: list[str]) -> list[list[str]]:
    blocks = [[]]
    block_idx = 0
    for l in input_lines:
        if l != '':
            blocks[block_idx].append(l)
        else:
            blocks.append([])
            block_idx += 1
    return blocks


def find_symmetry(blocks: list[list[str]]) -> int:
    matching_numbers = []
    for b_idx, block in enumerate(blocks):
        direction = ''
        match_per_block = {}
        curr_num = 0
        # test for a horizontal line reflection
        horizontal_line = None
        matchings = []
        for i, curr_line in enumerate(block):
            # for this line: find last appearance of same line in block
            for j, check_line in enumerate(block):
                if i != j and curr_line == check_line:
                    # also check if the lines in between also are the same, going inside
                    line_check = True
                    for n1 in range(i + 1, j):
                        for n2 in range(j - 1, i, -1):
                            if not block[n1] == block[n2]:
                                # line check not correct
                                line_check = False

                    if line_check:
                        # search for another occurrence
                        matchings = [i, j]
        if len(matchings) == 2 and not (matchings[0] == 0 or matchings[0] == len(block)-1 or matchings[1] == 0 or matchings[1] == len(block)-1):
            matchings = None
        else:
            match_per_block['hori'] = matchings
        if matchings:
            print(b_idx, matchings)
            distance = int(abs(matchings[0] + matchings[1]) / 2 + .5)
            # int(abs(matchings[0] + matchings[1]) / 2 + .5)
            horizontal_line = max([0, distance])
            curr_num = horizontal_line * 100
            direction = 'hori'
            matching_numbers.append(curr_num)
        # find vertical line mirror
        vertical_line = None
        matchings = []
        for i in range(len(block[0])):
            curr_line = ''.join([l[i] for l in block])
            # for this line: find last appearance of same line in block
            for j in range(len(block[0])):
                check_line = ''.join([l[j] for l in block])
                if i != j and curr_line == check_line:
                    line_check = True
                    for n1 in range(i + 1, j):
                        for n2 in range(j - 1, i, -1):
                            if not ''.join([l[n1] for l in block]) == ''.join([l[n2] for l in block]):
                                # line check not correct
                                line_check = False
                    if line_check:
                        # search for another occurrence
                        matchings = [i, j]
        if len(matchings) == 2 and not (matchings[0] == 0 or matchings[0] == len(block[0])-1 or matchings[1] == 0 or matchings[1] == len(block[0])-1):
            matchings = None
        else:
            match_per_block['verti'] = matchings
        if matchings:
            # print(b_idx, matchings)
            distance = int(abs(matchings[0] + matchings[1]) / 2 + .5)
            vertical_line = max([0, distance])
            # if vertical_line > curr_num / 100:
            direction = 'verti'
            curr_num = vertical_line
            matching_numbers.append(curr_num)
        for l in block:
            print(l)
        print(f'block: {b_idx}, direction: {direction}, {matchings}, {curr_num}')
        print('------------------------')
    return sum(matching_numbers)


if __name__ == '__main__':
    some_input_lines = load_codes()
    patterns = split_patterns(input_lines=some_input_lines)
    n = find_symmetry(blocks=patterns)
    pass
