import re


def load_codes() -> list[str]:
    with open('aoc_dec_4.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def get_wining_and_own_numbers(input_line: str) -> tuple[list[int], list[int]]:
    input_line = re.sub(r'Card *\d+: ', '', input_line)
    input_list = input_line.split(' ')

    wining_numbers_list = []
    own_number_list = []
    is_wining_number = True
    for s in input_list:
        if s != '':
            if is_wining_number:
                if s != '|':
                    wining_numbers_list.append(int(s))
                else:
                    is_wining_number = False
            else:
                own_number_list.append(int(s))
    return wining_numbers_list, own_number_list


def calc_total_score(input_lines: list[str]) -> int:
    score = 0
    for line in input_lines:
        successful_numbers = []
        wining_numbers, own_numbers = get_wining_and_own_numbers(input_line=line)
        for w in wining_numbers:
            if w in own_numbers:
                successful_numbers.append(w)
        score = score + (2 ** (len(successful_numbers) - 1)) if len(successful_numbers) > 0 else score + 0
    return score


if __name__ == '__main__':
    input_lines = load_codes()

    print(calc_total_score(input_lines))
    pass
