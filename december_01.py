"""
The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be
found by combining the first digit and the last digit (in that order) to form a single two-digit number.
"""
import re


def extract_digits(input: str) -> int:
    # extract digits from input string
    positive_replace = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for k in positive_replace.keys():
        a = [s.start() for s in re.finditer(k, input)]
        # insert beginning from the last
        a.reverse()
        for digit_idx in a:
            input = input[:digit_idx+1] + str(positive_replace[k]) + input[1+digit_idx:]

    numbers = re.findall('[0-9]', input)
    # get first and last number if exist and concat them together
    return int(numbers[0] + numbers[-1]) if len(numbers) else 0


def load_codes():
    with open('aoc_dec_1.txt') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    input_lines = load_codes()
    some_input_string = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

    print(sum([extract_digits(input_line) for input_line in input_lines]))

    # lambda abomination
    # print(sum([(lambda in_str: (digits := re.findall('\d', in_str), int(digits[0] + digits[-1]) if len(digits) else 0)[-1])(s) for s in input_lines]))
