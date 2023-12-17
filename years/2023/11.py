# day 11
from years.process import get_response, parse_response_to_array

raw_test_data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

test_data = parse_response_to_array(raw_test_data)

raw_data = get_response(day=11)
data = parse_response_to_array(raw_data)

def map_galaxies_by_row(rows):
    empty_columns = set(range(0, len(rows[0])))
    empty_rows = set()
    galaxies = set()
    for r_idx, r in enumerate(rows):
        empty_spaces = set()
        for idx, token in enumerate(r):
            if token == ".":
                empty_spaces.add(idx)
            else:
                galaxies.add((r_idx, idx))
        empty_columns = empty_columns.intersection(empty_spaces)
        if len(empty_spaces) == len(r):
            empty_rows.add(r_idx)
    return {
        "empty_columns": sorted(list(empty_columns)),
        "empty_rows": sorted(list(empty_rows)),
        "galaxies": galaxies
    }

def num_smaller(num, sorted_array):
    num_smaller = 0
    for item in sorted_array:
        if item < num:
            num_smaller += 1
        else:
            break
    return num_smaller

def apply_universe_growth(mapping):
    new_mapping = []
    for idx, g in enumerate(mapping["galaxies"]):
        row_adjustment = num_smaller(g[0], mapping["empty_rows"])
        column_adjustment = num_smaller(g[1], mapping["empty_columns"])
        new_mapping.append((g[0] + row_adjustment, g[1] + column_adjustment))
    return new_mapping
        
def get_pair_dist(galaxies):
    galaxies_to_compare = set(galaxies)
    total_dist = 0
    for g in galaxies:
        galaxies_to_compare.remove(g)
        total_dist += sum([abs(g[0] - gx) + abs(g[1] - gy) for (gx,gy) in galaxies_to_compare])
    return total_dist


def part_1(data):
    mapping = map_galaxies_by_row(data)
    galaxies = apply_universe_growth(mapping)
    return get_pair_dist(galaxies)

assert(part_1(test_data) == 374)

part_1 = part_1(data)
print(f"Part 1: {part_1}")

def apply_universe_growth_pt2(mapping, growth):
    new_mapping = []
    for idx, g in enumerate(mapping["galaxies"]):
        row_adjustment = max(0, num_smaller(g[0], mapping["empty_rows"]) * (growth - 1))
        column_adjustment = max(0, num_smaller(g[1], mapping["empty_columns"]) * (growth - 1))
        new_mapping.append((g[0] + row_adjustment, g[1] + column_adjustment))
    return new_mapping

def part_2(data, growth):
    mapping = map_galaxies_by_row(data)
    galaxies = apply_universe_growth_pt2(mapping, growth)
    return get_pair_dist(galaxies)

assert(part_2(test_data, 2) == 374)
assert(part_2(test_data, 10) == 1030)
assert(part_2(test_data, 100) == 8410)

part_2 = part_2(data, 1000000)
print(f"Part 2: {part_2}")