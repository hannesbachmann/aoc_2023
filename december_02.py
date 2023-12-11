"""
As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue.
Each time you play this game, he will hide a secret number of cubes of each color in the bag,
and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes,
the Elf will reach into the bag, grab a handful of random cubes,
show them to you, and then put them back in the bag.
He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input).
Each game is listed with its ID number (like the 11 in Game 11: ...)
followed by a semicolon-separated list of subsets of cubes that were revealed from the bag
(like 3 red, 5 green, 4 blue).

The Elf would first like to know which games would have been possible
if the bag contained only A red cubes, B green cubes, and C blue cubes?
"""
import re


def get_game_id(input_line: str) -> int:
    return int(re.findall(r'Game \d+', input_line)[0].replace('Game ', ''))


def separate_frames(input_line: str, game_id: int) -> list[str]:
    information_line = input_line.replace(f'Game {game_id}:', '').replace(' ', '')
    return information_line.split(';')


def count_colors_per_frame(frame: str) -> dict[str, int]:
    colors_count = {'red': 0, 'green': 0, 'blue': 0}
    color_str = {'red': [], 'green': [], 'blue': []}
    for color in color_str.keys():
        color_str[color] = re.findall(r'\d+' + color, frame)
        if len(color_str[color]):
            colors_count[color] = int(color_str[color][0].replace(color, ''))
    return colors_count


def game_is_possible(input_line: str, possible_game: dict[str, int]) -> int:
    current_game_id = get_game_id(input_line)
    frames = separate_frames(input_line, current_game_id)
    for frame in frames:
        c_per_frame = count_colors_per_frame(frame)
        for color in c_per_frame.keys():
            if not 0 <= c_per_frame[color] <= possible_game[color]:
                return 0
    return current_game_id


def calc_sum_of_possible_games(input_lines: list[str], possible_game: dict[str, int]) -> int:
    cumulative_sum_of_possible_game_ids = 0
    for line in input_lines:
        game_status = game_is_possible(line, possible_game)
        cumulative_sum_of_possible_game_ids += game_status
    return cumulative_sum_of_possible_game_ids


def fewest_possible_per_color_per_game(input_line: str) -> dict[str, int]:
    fewest_count = {'red': 0, 'green': 0, 'blue': 0}
    current_game_id = get_game_id(input_line)
    frames = separate_frames(input_line, current_game_id)
    for frame in frames:
        c_per_frame = count_colors_per_frame(frame)
        for color in c_per_frame.keys():
            if c_per_frame[color] >= fewest_count[color]:
                fewest_count[color] = c_per_frame[color]
    print(current_game_id, fewest_count)
    return fewest_count


def calculate_fewest_set_power_sum(input_lines: list[str]) -> int:
    cumulative_sum_set_power = 0
    for line in input_lines:
        few = fewest_possible_per_color_per_game(line)
        set_power = 1
        for color in few.keys():
            set_power *= few[color]
        cumulative_sum_set_power += set_power
    return cumulative_sum_set_power


def load_codes() -> list[str]:
    with open('aoc_dec_02.txt') as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    possible_game_colors = {'red': 12, 'green': 13, 'blue': 14}
    input_lines = load_codes()

    print(calculate_fewest_set_power_sum(input_lines))

    print(calc_sum_of_possible_games(input_lines, possible_game_colors))

    pass
