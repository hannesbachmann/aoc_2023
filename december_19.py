import re


def load_codes() -> list[str]:
    with open('aoc_dec_19.txt') as f:
        lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    return lines


def parse_input(input_lines: list[str]) -> tuple[dict[dict[str, str]], list[dict[str, int]]]:
    parts = []
    workflows = {}
    wf = True
    for line in input_lines:
        if line == '':
            wf = False
        else:
            if wf:
                name = re.findall(r'[a-z]+', line)[0]
                rules = [rule for rule in re.findall(r'\{.+}', line)[0].replace('}', '').replace('{', '').split(',')]
                workflow = {}
                for rule in rules:
                    s = rule.split(':')
                    if len(s) > 1:
                        workflow[s[0]] = s[1]
                    else:
                        workflow['otherwise'] = s[0]
                workflows[name] = workflow
            else:
                parts.append({con.split('=')[0]: int(con.split('=')[1]) for con in
                              line.replace('}', '').replace('{', '').split(',')})
    return workflows, parts


def evaluate_by_string(x: int, eva_string: str, result: str) -> str:
    if '<' in eva_string:
        if len(re.findall(r'\d+', eva_string)) and x < int(re.findall(r'\d+', eva_string)[0]):
            return result
    if '>' in eva_string:
        if len(re.findall(r'\d+', eva_string)) and x > int(re.findall(r'\d+', eva_string)[0]):
            return result
    if 'else' in eva_string:
        return result
    return ''


def do_work(work_flows: dict[dict[str, str]], part_list: list[dict[str, int]]) -> int:
    results = []

    for part in part_list:
        curr_wf = work_flows['in']
        while 1:
            for rule in curr_wf.keys():
                if rule[0] != 'o':
                    x = part[rule[0]]
                    curr_res = evaluate_by_string(x=x, eva_string=rule, result=curr_wf[rule])
                else:
                    curr_res = curr_wf['otherwise']
                if curr_res != '':
                    break
            if curr_res == 'A':
                results.append(1)
                break
            elif curr_res == 'R':
                results.append(0)
                break
            curr_wf = work_flows[curr_res]
    return sum([sum(part_list[i].values()) * results[i] for i in range(len(part_list))])


if __name__ == '__main__':
    some_input_lines = load_codes()
    w, p = parse_input(some_input_lines)
    # -- part 1 --
    print(f"part 1: {do_work(work_flows=w, part_list=p)}")
    # -- part 2 --
    print(f"part 2 {0}")
