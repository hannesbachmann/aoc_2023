import re
import numpy as np


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
                if line[i-1] == '.' and (line[i] == 'O' or line[i].isdigit()):
                    # swap
                    tmp_l = line[i-1]
                    line[i-1] = line[i]
                    line[i] = tmp_l
    return input_lines


# #################################################
# #################### PART 2 #####################
# #################################################
def one_cycle(input_lines):
    # north, then west, then south, then east per cycle
    repeatings = [np.array(input_lines)]
    cycle_found = 0
    for i in range(1000000000):
        input_lines = list(zip(*go_north(list(zip(*input_lines)))))   # go north
        input_lines = list(zip(*go_north(input_lines)))  # go west
        input_lines = go_north([reversed(line) for line in input_lines])   # south
        input_lines = go_north([reversed(line) for line in list(zip(*input_lines))])    # go east

        input_lines = [list(reversed(line)) for line in list(reversed(input_lines))]

        for idx, r in enumerate(repeatings):
            # search for a cycle after only a few runs, to calculate the high numbers later on
            # idx 3 == 9 -> from there on cyclic
            # 3 == 9 -> 4 == 10 -> 5 == 11 -> 6 == 12 -> 7 == 13 -> 8 == 14 -> 3 == 9 == 15 ->
            v = (np.array(input_lines) == r).all()
            if v:
                print(f'hey! {idx}, {i}')
                # cyc = 96
                # twice = 118
                twice = i + 1
                cycle_found = idx
                print(f'twice: {twice}, cycle: {cycle_found}')
                repeatings.append(np.array(input_lines))
                break
        repeatings.append(np.array(input_lines))
        if cycle_found:
            break

    after_go = repeatings[(1000000000 - cycle_found) % (twice - cycle_found) + cycle_found].tolist()

    return after_go


if __name__ == '__main__':
    some_input_lines = load_codes()
    # -- part 1 --
    print(f"part 1: {sum([len(re.findall(r'O', ''.join(line))) * (f+1) for f, line in enumerate(list(reversed(list(zip(*go_north(list(zip(*some_input_lines))))))))])}")
    # -- part 2 --
    print(f"part 2 {sum([len(re.findall(r'O', ''.join(line))) * (f+1) for f, line in enumerate(list(reversed(one_cycle([[c for c in line] for line in some_input_lines]))))])}")
    pass
