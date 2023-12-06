import re


def load_codes() -> list[str]:
    with open('aoc_dec_6.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_times_and_distance(input_lines: list[str]) -> tuple[list[int], list[int]]:
    times = [int(i) for i in re.findall(r'\d+', re.sub(r'Time: +', '', input_lines[0]))]
    distances = [int(i) for i in re.findall(r'\d+', re.sub(r'Distance: +', '', input_lines[1]))]
    return times, distances


def calc_options_t_d_pair(time: int, distance: int) -> tuple[list[int], list[int]]:
    scores = []
    winning_hold_times = []
    for time_hold in range(time + 1):
        scores.append(time_hold * (time - time_hold))
        if scores[time_hold] > distance:
            winning_hold_times.append(scores[time_hold])
    return scores, winning_hold_times


def calc_check_value(input_lines: list[str]) -> int:
    times, distances = parse_times_and_distance(input_lines=input_lines)
    check_value = 1
    for time, distance in zip(times, distances):
        scores, winning = calc_options_t_d_pair(time, distance)
        check_value *= len(winning)
    return check_value


if __name__ == '__main__':
    input_lines = load_codes()
    print(calc_check_value(input_lines=input_lines))
    pass
