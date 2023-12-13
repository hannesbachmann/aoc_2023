import re
import itertools


def load_codes() -> list[str]:
    with open('test_02.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_lines(input_lines: list[str]) -> tuple[list[str], list[list[str]]]:
    information_lines = []
    conditions = []
    for line in input_lines:
        conditions.append(re.findall(r'\d+', line))
        information_lines.append(re.findall(r'[#|\.|\?]+', line)[0])
    return information_lines, conditions


def calc_combination_that_hold_condition(information_lines: list[str], conditions: list[list[str]]) -> int:
    # calculate all possible combinations for assigning '.' and '#' to '?',
    # then check whether the condition for that line is hold or not
    new_lines = []
    for i, line in enumerate(information_lines):
        all_qm = [p.span()[0] for p in re.finditer(r'\?', line)]

        # go thought all combinations -> check conditions
        combinations = [com for com in itertools.product(['.', '#'], repeat=len(all_qm))]
        # filter not possible options based on conditions


        combi_lines = []
        for combi in combinations:
            # replacing
            curr_line = line
            for qm in range(len(all_qm)):
                curr_line = curr_line[:all_qm[qm]] + combi[qm] + curr_line[all_qm[qm]+1:]
                # curr_line = curr_line.replace('?', combi[qm], qm + 1)
            combi_lines.append(curr_line)
        new_lines.append(combi_lines)

    # another idea: using a sliding window
    # for i, line in enumerate(information_lines):
    #     current_check = 0
    #     tmp_window = ''
    #     for c in line:
    #         if c != '.':
    #             tmp_window += c
    #             if len(tmp_window) > int(conditions[i][current_check]):
    #                 tmp_window = tmp_window[1:]
    #         else:
    #             tmp_window = ''
    #         print(tmp_window)
    #     pass

    return 0


def condition_is_hold(line: str, condition: list[str]) -> bool:
    current_condition_pointer = 0
    current_tmp_s = ''
    for c in line:
        if c != '.':
            current_tmp_s += c


    return True


from time import time
from functools import cache


@cache
def run(row, record):
    if len(row) == 0: return len(record) == 0
    if len(record) == 0: return not '#' in row
    if row[0] == '.': return run(row[1:], record)
    ret = 0
    if row[0] == '?':
        ret += run(row[1:], record)
    if not '.' in row[:record[0]] and (len(row) > record[0] and row[record[0]] != '#' or len(row) == record[0]):
        ret += run(row[record[0] + 1:], record[1:])
    return ret




if __name__ == '__main__':
    start = time()
    data = open("aoc_dec_12.txt").read().split('\n')

    print(sum(run(line.split()[0], tuple(int(r) for r in line.split()[1].split(','))) for line in data))
    print(sum(
        run('?'.join([line.split()[0]] * 5), tuple(int(r) for r in line.split()[1].split(',')) * 5) for line in data))

    print(f"\n===== {time() - start} sec =====")
    # some_input_lines = load_codes()
    # info_lines, cons = parse_lines(input_lines=some_input_lines)
    # n = calc_combination_that_hold_condition(information_lines=info_lines, conditions=cons)
    pass
