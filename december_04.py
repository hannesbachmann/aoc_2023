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


def calc_number_of_cards(input_lines: list[str]) -> int:
    successful_numbers = {}
    i = 0
    for line in input_lines:
        i += 1
        wining_numbers, own_numbers = get_wining_and_own_numbers(input_line=line)
        successful_numbers[f'{i}'] = 0
        for w in wining_numbers:
            if w in own_numbers:
                successful_numbers[f'{i}'] += 1
    # calculate cards which gets added
    count_per_card = {f'{i+1}': 1 for i in range(len(input_lines))}
    for line_idx in range(len(input_lines)):
        cards_to_add = list(range(line_idx+2, line_idx+2+successful_numbers[str(line_idx+1)]))
        for i in range(count_per_card[str(line_idx+1)]):
            for c in cards_to_add:
                count_per_card[str(c)] += 1
    number_of_cards = sum([count_per_card[k] for k in count_per_card.keys()])
    return number_of_cards


if __name__ == '__main__':
    input_lines = load_codes()
    print(calc_number_of_cards(input_lines=input_lines))

    print(calc_total_score(input_lines))
    pass
