"""

"""
import re


def load_codes() -> list[str]:
    with open('aoc_dec_03.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def find_numbers(input_line: str) -> dict[str, dict[str, int]]:
    numbers = re.finditer(r'\d+', input_line)
    number_positions = {}
    for num in numbers:
        match = num.span()
        number_positions[num.group()] = {'start': match[0], 'end': match[1]}
    return number_positions


def get_neighborhood(input_lines: list[str], line_idx: int, number_start: int, number_end: int) -> list[str]:
    previous_line = input_lines[line_idx-1] if line_idx >= 1 else None
    current_line = input_lines[line_idx]
    next_line = input_lines[line_idx+1] if line_idx <= len(input_lines) - 2 else None
    neighborhood_symbols = []
    if number_start >= 1:
        neighborhood_symbols.append(current_line[number_start-1])
    if number_end <= len(current_line) - 1:
        neighborhood_symbols.append(current_line[number_end])
    start_pos = number_start - 1 if number_start >= 1 else 0
    end_pos = number_end if number_end <= len(current_line) - 1 else number_end - 1
    for pos in range(start_pos, end_pos + 1):
        if previous_line is not None:
            neighborhood_symbols.append(previous_line[pos])
        if next_line is not None:
            neighborhood_symbols.append(next_line[pos])

    return neighborhood_symbols


def is_symbol_in_neighborhood(neighborhood_list: list[str]) -> bool:
    neighborhood_str = ''.join(neighborhood_list)
    neighborhood_str = neighborhood_str.replace('.', '')
    return bool(len(neighborhood_str))


def calc_engine_schematic(input_lines: list[str]) -> int:
    good_numbers = []
    for line_idx in range(len(input_lines)):
        numbers = find_numbers(input_lines[line_idx])
        for num in numbers.keys():
            neighborhood = get_neighborhood(input_lines, line_idx, numbers[num]['start'], numbers[num]['end'])
            if is_symbol_in_neighborhood(neighborhood):
                good_numbers.append(num)

    return sum([int(n) for n in good_numbers])


if __name__ == '__main__':
    input_lines = load_codes()

    print(calc_engine_schematic(input_lines))
    pass
