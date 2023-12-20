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


# #################################################
# #################### PART 1 #####################
# #################################################
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


# #################################################
# #################### PART 2 #####################
# #################################################
def find_accepting_combinations(work_flows):
    # find wf that are accepting ends
    acceptings = {}
    for wf in work_flows.keys():
        if 'A' in list(work_flows[wf].values()):
            acceptings[wf] = work_flows[wf]
    for acc in acceptings.keys():
        # for every occurrence of 'A' in accepting workflows: find conditions that need to be satisfied to get there
        tmp_workflow = {}
        for rule in acceptings[acc].keys():
            tmp_workflow[rule] = acceptings[acc][rule]
            if acceptings[acc][rule] == 'A':
                x, m, a, s = extract_conditions(work_flow=tmp_workflow)
                print(x, m, a, s)
    pass


def extract_conditions(work_flow):
    # returns 4 ranges as teh conditions for workflows
    # take all current conditions into account
    x = range(1, 4000+1)
    m = range(1, 4000+1)
    a = range(1, 4000+1)
    s = range(1, 4000+1)
    for k in work_flow.keys():
        # x---------
        xx = x
        if 'x' in k and work_flow[k] == 'A':
            if '<' in k:
                xx = range(int(re.findall(r'\d+', k)[0]), 4000+1)
            elif '>' in k:
                xx = range(1, int(re.findall(r'\d+', k)[0])+1)
        elif 'x' in k and work_flow[k] != 'A':
            if '<' in k:
                xx = range(1, int(re.findall(r'\d+', k)[0]))
            elif '>' in k:
                xx = range(int(re.findall(r'\d+', k)[0])+1, 4000+1)
        x = list(set(x) & set(xx))
        # m---------
        mm = m
        if 'm' in k and work_flow[k] == 'A':
            if '<' in k:
                mm = range(int(re.findall(r'\d+', k)[0]), 4000+1)
            elif '>' in k:
                mm = range(1, int(re.findall(r'\d+', k)[0])+1)
        elif 'm' in k and work_flow[k] != 'A':
            if '<' in k:
                mm = range(1, int(re.findall(r'\d+', k)[0]))
            elif '>' in k:
                mm = range(int(re.findall(r'\d+', k)[0])+1, 4000+1)
        m = list(set(m) & set(mm))
        # a---------
        aa = a
        if 'a' in k and work_flow[k] == 'A':
            if '<' in k:
                aa = range(int(re.findall(r'\d+', k)[0]), 4000+1)
            elif '>' in k:
                aa = range(1, int(re.findall(r'\d+', k)[0])+1)
        elif 'a' in k and work_flow[k] != 'A':
            if '<' in k:
                aa = range(1, int(re.findall(r'\d+', k)[0]))
            elif '>' in k:
                aa = range(int(re.findall(r'\d+', k)[0])+1, 4000+1)
        a = list(set(a) & set(aa))
        # s---------
        ss = s
        if 's' in k and work_flow[k] == 'A':
            if '<' in k:
                ss = range(int(re.findall(r'\d+', k)[0]), 4000+1)
            elif '>' in k:
                ss = range(1, int(re.findall(r'\d+', k)[0])+1)
        elif 's' in k and work_flow[k] != 'A':
            if '<' in k:
                ss = range(1, int(re.findall(r'\d+', k)[0]))
            elif '>' in k:
                ss = range(int(re.findall(r'\d+', k)[0])+1, 4000+1)
        s = list(set(s) & set(ss))
        pass

    return list(x), list(m), list(a), list(s)


if __name__ == '__main__':
    some_input_lines = load_codes()
    w, p = parse_input(some_input_lines)
    # -- part 1 --
    print(f"part 1: {do_work(work_flows=w, part_list=p)}")
    # -- part 2 --
    print(f"part 2 {find_accepting_combinations(work_flows=w)}")
    pass