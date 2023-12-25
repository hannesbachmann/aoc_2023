from __future__ import annotations

import re
from collections import deque


def load_codes() -> list[str]:
    with open('aoc_dec_20.txt') as f:
        lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    return lines


def parse_input(input_lines: list[str]) -> tuple[list[list[str]], dict[str, dict[str, list[str]]]]:
    broadcasters = []
    modules = {}
    for line in input_lines:
        destinations = re.findall(r'-> .+', line)[0].replace('-> ', '').replace(' ', '').split(',')
        if line.startswith('b'):
            broadcasters.append(destinations)
        elif line.startswith('%'):
            name = re.findall(r'%[a-z]+', line)[0].replace('%', '')
            modules[name] = {'type': '%', 'state': 0, 'destinations': destinations}
        elif line.startswith('&'):
            # this conjunction acts just like a nand (sending low when it receives only high values as input)
            # one input high: send low
            name = re.findall(r'&[a-z]+', line)[0].replace('&', '')
            modules[name] = {'type': '&', 'inputs': [], 'destinations': destinations}
    return broadcasters, modules


class Conjunction:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.old_inputs = {}  # parent_id, value

    def add_parent(self, parent_id):
        self.old_inputs[parent_id] = 0

    def evaluate(self, signal, parent_id) -> int:
        """
        returns high(1) or low(0)
        case every old parent evaluates to high(1): return low
        otherwise: return high
        """
        self.old_inputs[parent_id] = signal
        if all(i == 1 for i in list(self.old_inputs.values())):
            return 0
        return 1


class FlipFlop:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.state = 'OFF'

    def evaluate(self, signal, parent_id=None) -> int | None:
        """
        case send high: send low, state stays the same
        case state is OFF: low->high, state->ON
        case state is ON: low->low,  state->OFF
        """
        # receive high: send low, state stays the same
        if signal:
            return None
        # ON: low->low, state->OFF
        if self.state == 'ON':
            self.state = 'OFF'
            return 0
        # OFF: low->high, state->ON
        self.state = 'ON'
        return 1


class Broadcast:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def evaluate(self, signal, parent_id=None):
        return signal


class Button:
    def __init__(self, name):
        self.name = name
        self.signal = 0

    def evaluate(self, signal=None, parent_id=None):
        return self.signal


class Circuit:
    def __init__(self, broadcasts, modules):
        self.circuit_modules = {}
        self.build_circuit(broadcasts, modules)
        self.__result = self.press_button()

    def get_result(self):
        return self.__result

    def build_circuit(self, broadcasts, modules):
        self.circuit_modules['but'] = Button('but')
        for i, b in enumerate(broadcasts):
            # button is the parent here
            self.circuit_modules[f'bc{i}'] = Broadcast(f'bc{i}', b)
        for m in modules.keys():
            self.circuit_modules[m] = self.build_block(m, modules[m]['type'], modules[m]['destinations'])
        # get all parents for each conjunction module
        for m in modules.keys():
            if modules[m]['type'] == '&':
                if m in broadcasts[0]:
                    self.circuit_modules[m].add_parent('bc0')
                for n in modules.keys():
                    if m in modules[n]['destinations']:
                        self.circuit_modules[m].add_parent(n)
        pass

    def build_block(self, name, m_type, destinations):
        if m_type == '&':
            return Conjunction(name, destinations)
        else:
            return FlipFlop(name, destinations)

    def press_button(self):
        values = []
        num_press_button = 1000
        for i in range(num_press_button):
            # press the button again
            curr_value = self.circuit_modules['but'].evaluate()
            values.append(curr_value)
            print('but' + '-' + str(curr_value) + '->' + 'bc0')
            curr_value = self.circuit_modules['bc0'].evaluate(curr_value)
            q = deque()
            for module in self.circuit_modules['bc0'].destinations:
                # value, source_id, target
                print('bc0' + ' -' + str(curr_value) + '-> ' + module)
                values.append(curr_value)
                q.append([curr_value, 'bc0', module])
            while len(q) > 0:
                q_len = len(q)
                q_buff = [q.popleft() for i in range(q_len)]
                for b in q_buff:
                    # 0: value
                    # 1: source_id
                    # 2: target_id
                    # b[2] must be an output module when target not in keys
                    if b[2] in self.circuit_modules:
                        value = self.circuit_modules[b[2]].evaluate(b[0], b[1])
                        if value is not None:
                            # value is None in case of a flipflop receives a high input
                            for destination in self.circuit_modules[b[2]].destinations:
                                q.append([value, b[2], destination])
                                print(b[2] + ' -' + str(value) + '-> ' + destination)
                                values.append(value)
        return values.count(0) * values.count(1)


if __name__ == '__main__':
    some_input_lines = load_codes()
    bc, m = parse_input(some_input_lines)
    C = Circuit(bc, m)
    # -- part 1 --
    print(f"part 1: {C.get_result()}")
    # -- part 2 --
    print(f"part 2 {0}")
    pass
