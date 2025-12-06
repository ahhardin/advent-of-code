from years.process import *

test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

real_input = get_response(day=5, year=2025)

def process_input(raw_data):
    groups, ingredients = raw_data.strip().split("\n\n")
    groups = groups.strip().split("\n")
    groups = [[int(split) for split in group.split("-")] for group in groups]
    ingredients = [int(s) for s in ingredients.strip().split("\n")]
    return set([tuple(group) for group in groups]), ingredients
  

def check_inclusion_in_group(number, group):
    return group[0] <= number <= group[1]

def part_1(raw_data):
    groups, ingredients = process_input(raw_data)
    num_fresh = 0
    for ingredient in ingredients:
        for group in groups:
            if check_inclusion_in_group(ingredient, group):
                num_fresh += 1
                break
    return num_fresh


assert part_1(test_input) == 3
print(f"Part 1: {part_1(real_input)}")

def is_overlap(range_1, range_2):
    no_overlap_top = range_1[0] > range_2[1]
    no_overlap_bottom = range_1[1] < range_2[0]
    return not(no_overlap_top or no_overlap_bottom)

def merge_ranges(range_1, range_2):
    return tuple([min(range_1[0], range_2[0]), max(range_1[1], range_2[1])])

# tests
assert is_overlap((0,5),(6,10)) == False
assert is_overlap((7,50), (87,500)) == False
assert is_overlap((7,20), (18,20)) == True
assert is_overlap((7,20), (2,7)) == True

assert merge_ranges((7,20), (18,20)) == (7,20)
assert merge_ranges((7,20), (2,7)) == (2,20)

def process_merging(groups):
    new_groups = set()
    total_merges = 0
    for group_1 in groups:
        merges = 0
        for group_2 in groups:
            if group_1 == group_2:
                continue
            # check overlap and merge if needed
            if is_overlap(group_1, group_2):
                new_groups.add(merge_ranges(group_1, group_2))
                merges +=1
                total_merges += 1
        if not merges:
            new_groups.add(group_1)
    if total_merges: 
        return process_merging(new_groups)
    return new_groups

def part_2(raw_data):
    groups, _ = process_input(raw_data)
    new_groups = process_merging(groups)
    count = 0
    for group in new_groups:
        group_size = group[1] - group[0] + 1
        count += group_size
    return count


assert part_2(test_input) == 14
print(f"Part 2: {part_2(real_input)}")