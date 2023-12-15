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


def calc_sequence_sum_p1(init_s) -> int:
    return sum([list(itertools.accumulate('.' + s, lambda previous, current: ((previous + ord(
        current)) * 17) % 256 if isinstance(
        previous, int) else ((0 + ord(current)) * 17) % 256))[-1] for s in init_s])


def calc_hash(s):
    return list(itertools.accumulate('.' + re.findall(r'[a-zA-Z]+', s)[0], lambda previous, current: ((previous + ord(
        current)) * 17) % 256 if isinstance(
        previous, int) else ((0 + ord(current)) * 17) % 256))[-1]


def calc_focusing_powers(init_s) -> int:
    boxes = [[] for i in range(256)]
    for seq in init_s:
        box = calc_hash(seq)
        label = re.findall(r'[a-zA-Z]+', seq)[0]
        if seq.endswith('-'):
            for n in range(len(boxes[box])):
                if label == boxes[box][n][0]:
                    boxes[box].pop(n)
                    break
        else:
            focus = re.findall(r'\d+', seq)[0]
            l_found = False
            for n in range(len(boxes[box])):
                if label == boxes[box][n][0]:
                    boxes[box][n][1] = focus
                    l_found = True
            if not l_found:
                boxes[box].append([label, focus])
    # final focus calculation
    focus = []
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focus.append((i+1)*(j+1)*int(lens[1]))
    return sum(focus)


if __name__ == '__main__':
    # -- part 1 --
    print(f"part 1: {sum([list(itertools.accumulate('.' + s, lambda p, c: ((p + ord(c)) * 17) % 256 if isinstance(p, int) else ((0 + ord(c)) * 17) % 256))[-1] for s in load_codes()[0].split(',')])}")
    # -- part 2 --
    print(f"part 2: {calc_focusing_powers(init_sequence(input_lines=load_codes()))}")
    pass
