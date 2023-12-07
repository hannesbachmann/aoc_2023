import re


def load_codes() -> list[str]:
    with open('aoc_dec_5.txt') as f:
        lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]
    return lines


def separate_by_empty_lines(input_lines: list[str]) -> list[list[str]]:
    frames = [[]]
    frame_idx = 0
    for line in input_lines:
        if not line == '':
            frames[frame_idx].append(line)
        else:
            frames.append([])
            frame_idx += 1
    return frames


def get_seeds(seed_lines: list[str]) -> list[int]:
    seeds_list = []
    seed_lines[0] = re.sub(r'seeds: ', '', seed_lines[0])
    for line in seed_lines:
        seeds_list = seeds_list + re.findall(r'\d+', line)
    return seeds_list


def get_seed_ranges(seeds_list: list[int]) -> list[list[int]]:
    seed_ranges = []
    i = 0
    current_pair = []
    for seed in seeds_list:
        current_pair.append(seed)
        if i % 2 == 1:
            seed_ranges.append(range(current_pair[0], current_pair[0] + current_pair[1]))
            current_pair = []
        i += 1
    return seed_ranges


def get_source_destination_mapping(input_lines: list[str]) -> list[dict[str, tuple[int, int]]]:
    source_destination_dict = []
    for line in input_lines[1:]:
        numbers = [int(s) for s in re.findall(r'\d+', line)]
        source_destination_dict.append({'destinations_interval': (numbers[0], numbers[0] + numbers[2] - 1),
                                        'sources_interval': (numbers[1], numbers[1] + numbers[2] - 1)})
    return source_destination_dict


def map_source_to_destination(input_num: int, sources: list[tuple[int, int]], destinations: list[tuple[int, int]]) -> int:
    out = int(input_num)
    for i in range(len(sources)):
        if sources[i][0] <= int(input_num) <= sources[i][1]:
            # use this as corresponding destination
            out = destinations[i][0] + (int(input_num) - sources[i][0])
    return out


def calc_min_locations(input_lines: list[str]) -> int:
    frames = separate_by_empty_lines(input_lines=input_lines)
    seeds = get_seeds(seed_lines=frames[0])
    locations = []
    for seed in seeds:
        source = seed
        for frame in frames[1:]:
            mapping = get_source_destination_mapping(input_lines=frame)
            destination = map_source_to_destination(input_num=source,
                                                    sources=[seso['sources_interval'] for seso in mapping],
                                                    destinations=[seso['destinations_interval'] for seso in mapping])
            source = destination
        locations.append(source)
    min_location = min(locations)
    return min_location


def calc_min_location_seed_ranges(input_lines: list[str]) -> int:
    frames = separate_by_empty_lines(input_lines=input_lines)
    seeds = [int(s) for s in get_seeds(seed_lines=frames[0])]
    locations = []
    seeds = get_seed_ranges(seeds_list=seeds)

    with open('aoc_dec_5.txt') as f:
        _, *mappings = f.read().split("\n\n").copy()
    for m in mappings[1:]:
        if m == '':
            continue
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
        new_seeds = []

        for r in seeds:
            for tr, fr in ranges:
                offset = tr.start - fr.start
                if r.stop <= fr.start or fr.stop <= r.start:
                    continue
                ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
                lr = range(r.start, ir.start)
                rr = range(ir.stop, r.stop)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                new_seeds.append(r)

        seeds = new_seeds

    return min(x.start for x in seeds)


def pairs(l):
    it = iter(l)
    return zip(it, it)


if __name__ == '__main__':
    input_lines = load_codes()

    min_loc_from_range = calc_min_location_seed_ranges(input_lines=input_lines)
    print(min_loc_from_range)

    min_loc = calc_min_locations(input_lines=input_lines)
    print(min_loc)

    pass
