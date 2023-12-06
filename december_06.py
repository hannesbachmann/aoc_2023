import re


def load_codes() -> list[str]:
    with open('aoc_dec_6.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines

##################################################
##################### PART 1 #####################
##################################################
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


##################################################
##################### PART 2 #####################
##################################################
def parse_time_distance_p2(input_lines: list[str]) -> tuple[int, int]:
    time = int(re.sub(r'Time: +', '', input_lines[0]).replace(' ', ''))
    distance = int(re.sub(r'Distance: +', '', input_lines[1]).replace(' ', ''))
    return time, distance


def number_of_options(input_lines: list[str]) -> int:
    time, distance = parse_time_distance_p2(input_lines=input_lines)
    # time_hold * (time - time_hold) must be higher than distance
    # strategy: calculate until the first value is higher.
    #           then search from the last time value to get upper limit
    first_success = 0
    for time_hold in range(time + 1):
        if time_hold * (time - time_hold) > distance:
            first_success = time_hold
            break
    t_tmp = time
    last_success = time
    while t_tmp >= 0:
        if t_tmp * (time - t_tmp) > distance:
            last_success = t_tmp
            break
        t_tmp -= 1
    return last_success - first_success + 1


if __name__ == '__main__':
    input_lines = load_codes()
    no = number_of_options(input_lines=input_lines)
    print(no)

    print(calc_check_value(input_lines=input_lines))
    pass
