import re
import numpy as np
import itertools


def load_codes() -> list[str]:
    with open('aoc_dec_15.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def init_sequence(input_lines):
    return input_lines[0].split(',')


def calc_sequence_sum_p1(init_sequence) -> int:
    return sum([list(itertools.accumulate('.' + s, lambda previous, current: ((previous + ord(
        current)) * 17) % 256 if isinstance(
        previous, int) else ((0 + ord(current)) * 17) % 256))[-1] for s in init_sequence])


if __name__ == '__main__':
    # some_input_lines = load_codes()
    # init_seq = init_sequence(input_lines=some_input_lines)
    # -- part 1 --
    print(f"part 1: {sum([list(itertools.accumulate('.' + s, lambda p, c: ((p + ord(c)) * 17) % 256 if isinstance(p, int) else ((0 + ord(c)) * 17) % 256))[-1] for s in load_codes()[0].split(',')])}")
    # 508498
    pass
