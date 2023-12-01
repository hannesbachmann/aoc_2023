"""
The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be
found by combining the first digit and the last digit (in that order) to form a single two-digit number.
"""
import re


def extract_digits(input: str) -> int:
    # extract digits from input string
    numbers = re.findall('[0-9]', input)
    # get first and last number if exist
    return int(numbers[0] + numbers[-1]) if len(numbers) else 0


if __name__ == '__main__':
    some_input_string = 'ab822c4de5f'

    print((lambda in_str: (x := re.findall('\d', in_str), int(x[0] + x[-1]) if len(x) else 0)[-1])(some_input_string))
