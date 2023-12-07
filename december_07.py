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


def compare_p2(xs: dict[str: int], ys: dict[str: int]) -> 1 | -1:
    # ! now there is a Joker 'J' that is assigned to the best set option but a single joker is threaded as weakest card
    # compare by set rules
    # test on set conditions and assign corresponding values:
    # five of a kind:   7
    # four of a kind:   6
    # full house:       5
    # three of a kind:  4
    # two pair:         3
    # one pair:         2
    # high card:        1
    xs_wo_j = list(xs.keys())[0].replace('J', '')
    ys_wo_j = list(ys.keys())[0].replace('J', '')

    duplicates = [list({c: xs_wo_j.count(c) for c in xs_wo_j}.values()),
                  list({c: ys_wo_j.count(c) for c in ys_wo_j}.values())]
    # like before calculate the set score without considering the Jokers as part of any set
    set_scores = [1, 1]
    for i, d in enumerate(duplicates):
        set_scores[i] = 2 if 2 in d else set_scores[i]
        set_scores[i] = 3 if 2 in list({c: d.count(c) for c in set(d)}.values()) else set_scores[i]
        set_scores[i] = 4 if 3 in d else set_scores[i]
        set_scores[i] = 5 if 3 in d and 2 in d else set_scores[i]
        set_scores[i] = 6 if 4 in d else set_scores[i]
        set_scores[i] = 7 if 5 in d else set_scores[i]
    # get number of Jokers
    jokers = [{c: list(xs.keys())[0].count(c) for c in set(list(xs.keys())[0])}['J'] if 'J' in list(xs.keys())[0] else 0,
              {c: list(ys.keys())[0].count(c) for c in set(list(ys.keys())[0])}['J'] if 'J' in list(ys.keys())[0] else 0]
    print('------------------')
    print(f'before: {set_scores[0]}')
    # assign Jokers to sets
    for i in range(len(set_scores)):
        if jokers[i] == 5:
            # five of a kind in jokers
            set_scores[i] = 7
            continue
        if set_scores[i] == 6 and jokers[i] == 1:
            # four of a kind
            set_scores[i] = 7
        elif set_scores[i] == 5:
            # full house
            set_scores[i] = 5 + jokers[i]
        elif set_scores[i] == 4:
            # three of a kind
            if jokers[i] > 0:
                set_scores[i] = 4 + jokers[i] + 1
        elif set_scores[i] == 3:
            # two pair
            if jokers[i] == 1:
                # create a full house
                set_scores[i] = 5
        elif set_scores[i] == 2:
            # one pair
            if jokers[i] == 1:
                set_scores[i] = 4
            elif jokers[i] == 2:
                set_scores[i] = 6
            elif jokers[i] == 3:
                set_scores[i] = 7
        elif set_scores[i] == 1:
            # high card
            if jokers[i] == 1:
                set_scores[i] = 2
            elif jokers[i] == 2:
                set_scores[i] = 4
            elif jokers[i] == 3:
                set_scores[i] = 6
            elif jokers[i] == 4:
                set_scores[i] = 7
            elif jokers[i] == 5:
                set_scores[i] = 7
    print(list(xs.keys())[0], set_scores[0])
    # 250861414
    # 250665248
    if set_scores[0] == set_scores[1]:
        # compare by card values
        c_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
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
    hands = [{line.split(' ')[0]: int(line.split(' ')[1])} for line in input_lines]
    hands_s = sorted(hands, key=functools.cmp_to_key(compare_p2))  # sort with rising score (high index == high score)
    return sum([(i + 1) * list(hand.values())[0] for i, hand in enumerate(hands_s)])


if __name__ == '__main__':
    input_lines = load_codes()
    # -- part 1 --
    # print(calc_game_score_from_order_p1(input_lines=input_lines))

    # -- part 2 --
    print(calc_game_score_from_order_p2(input_lines=input_lines))

    pass
