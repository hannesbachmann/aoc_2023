from math import lcm
import re


def load_codes() -> list[str]:
    with open('aoc_dec_08.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def parse_input(input_lines: list[str]) -> tuple[str, dict[str, list[str]]]:
    part = 1
    traversal_sequence = ''
    edges = {}
    for l in input_lines:
        if l == '':
            part = 2
        elif part == 1:
            traversal_sequence += l
        elif part == 2:
            edges[re.findall(r"[A-Z]+", l)[0]] = [re.findall(r"[A-Z]+", l)[1], re.findall(r"[A-Z]+", l)[2]]
    return traversal_sequence, edges


def network_traversal(start_node: str, end_nodes: list[str], sequence: str, edges: dict[str, list[str]]) -> int:
    current_node = start_node
    steps = 0
    found = False
    while not found:
        for direction in sequence:
            if current_node in end_nodes:
                found = True
                break
            current_node = edges[current_node][0] if direction == 'L' else edges[current_node][1]
            steps += 1
    return steps


# #################################################
# #################### PART 1 #####################
# #################################################
def calc_number_of_steps_p1(input_lines: list[str]) -> int:
    tra_seq, edges = parse_input(input_lines=input_lines)
    return network_traversal(start_node='AAA', end_nodes=['ZZZ'], sequence=tra_seq, edges=edges)


# #################################################
# #################### PART 2 #####################
# #################################################
def calc_number_of_steps_p2(input_lines: list[str]) -> int:
    tra_seq, edges = parse_input(input_lines=input_lines)
    starting_nodes = [n for n in edges if n.endswith('A')]
    ending_nodes = [n for n in edges if n.endswith('Z')]
    steps_list = [network_traversal(start_node=node,
                                    end_nodes=ending_nodes,
                                    sequence=tra_seq, edges=edges) for node in starting_nodes]
    curr_steps = 1
    for step in steps_list:
        curr_steps = lcm(step, curr_steps)

    return curr_steps


if __name__ == '__main__':
    input_lines = load_codes()
    # -- part 1 --
    print(calc_number_of_steps_p1(input_lines=input_lines))
    # -- part 2 --
    print(calc_number_of_steps_p2(input_lines=input_lines))
    pass

# 22289513667691
# 22289513667691
# 22289513667691
