import re
import numpy as np


def load_codes() -> list[str]:
    with open('aoc_dec_15.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def init_sequence(input_lines):
    return input_lines[0].split(',')


def calc_sequence_sum_p1(init_sequence) -> int:
    part_sum = 0
    for s in init_sequence:
        seq_sum = 0
        for c in s:
            seq_sum += ord(c)
            seq_sum *= 17
            seq_sum = seq_sum % 256
        part_sum += seq_sum
        print(s, seq_sum)
    return part_sum


if __name__ == '__main__':
    some_input_lines = load_codes()
    init_seq = init_sequence(input_lines=some_input_lines)
    # -- part 1 --
    print(f'part 1: {calc_sequence_sum_p1(init_seq)}')
    # 508498
    pass
