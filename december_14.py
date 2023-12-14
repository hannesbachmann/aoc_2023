import re
import itertools


def load_codes() -> list[str]:
    with open('aoc_dec_14.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


# #################################################
# #################### PART 1 #####################
# #################################################
def go_north(input_lines):
    input_lines = [[c for c in line] for line in input_lines]
    for line in input_lines:
        for n in range(len(line)):
            for i in range(1, len(line)):
                if line[i-1] == '.' and line[i] == 'O':
                    # swap
                    line[i-1] = 'O'
                    line[i] = '.'
    return input_lines


if __name__ == '__main__':
    some_input_lines = load_codes()
    print(f"part 1: {sum([len(re.findall(r'O', ''.join(line))) * (f+1) for f, line in enumerate(list(reversed(list(zip(*go_north(list(zip(*some_input_lines))))))))])}")
    pass
