import functools
import re


def load_codes() -> list[str]:
    with open('aoc_dec_7.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def compare_p1(xs: dict[str: int], ys: dict[str: int]) -> 1 | -1:
    # compare by set rules
    # test on set conditions and assign corresponding values:
    # five of a kind:   7
    # four of a kind:   6
    # full house:       5
    # three of a kind:  4
    # two pair:         3
    # one pair:         2
    # high card:        1

    duplicates = [list({c: list(xs.keys())[0].count(c) for c in set(list(xs.keys())[0])}.values()),
                  list({c: list(ys.keys())[0].count(c) for c in set(list(ys.keys())[0])}.values())]
    set_scores = [1, 1]
    for i, d in enumerate(duplicates):
        set_scores[i] = 2 if 2 in d else set_scores[i]
        set_scores[i] = 3 if 2 in list({c: d.count(c) for c in set(d)}.values()) else set_scores[i]
        set_scores[i] = 4 if 3 in d else set_scores[i]
        set_scores[i] = 5 if 3 in d and 2 in d else set_scores[i]
        set_scores[i] = 6 if 4 in d else set_scores[i]
        set_scores[i] = 7 if 5 in d else set_scores[i]

    if set_scores[0] == set_scores[1]:
        # compare by card values
        c_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        for x, y in zip(list(xs.keys())[0], list(ys.keys())[0]):
            if x != y:
                return 1 if c_order.index(x) < c_order.index(y) else -1
    else:
        return 1 if set_scores[0] > set_scores[1] else -1
    return 1


# #################################################
# #################### PART 1 #####################
# #################################################
def calc_game_score_from_order_p1(input_lines: list[str]) -> int:
    hands = [{line.split(' ')[0]: int(line.split(' ')[1])} for line in input_lines]
    hands_s = sorted(hands, key=functools.cmp_to_key(compare_p1))  # sort with rising score (high index == high score)
    return sum([(i + 1) * list(hand.values())[0] for i, hand in enumerate(hands_s)])


# #################################################
# #################### PART 2 #####################
# #################################################
def calc_game_score_from_order_p2(input_lines: list[str]):
    return 2


if __name__ == '__main__':
    input_lines = load_codes()
    # -- part 1 --
    print(calc_game_score_from_order_p1(input_lines=input_lines))

    # -- part 2 --
    print(calc_game_score_from_order_p2(input_lines=input_lines))

    pass
