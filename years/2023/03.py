import regex as re

from collections import defaultdict

from years.process import get_response, parse_response_to_array

raw_test_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

PART_1_REGEX = "[^0-9.]"
PART_2_REGEX = "\*"

test_data = parse_response_to_array(raw_test_data)
data = parse_response_to_array(get_response(day=3))

# find all symbols and get coords
def get_symbol_locs_in_line(line, regex_string):
    match = re.finditer(regex_string, line)
    return tuple(m.start() for m in match)

def get_number_neighbors_in_line(line, line_id):
    # find all the possible neighbor coordinates for a number
    number_neighbors = []
    matches = re.finditer("[0-9]+", line)
    for match in matches:
        x1 = match.start()
        x2 = match.end()
        value = int(match.group())
        # ends
        neighbor_coords = set([
          (x1-1, line_id), (x2, line_id),
          (x1-1, line_id+1), (x2, line_id+1),
          (x1-1, line_id-1), (x2, line_id-1),
        ])
        # top and bottom
        for x in range(x1, x2):
            neighbor_coords.update([(x,line_id+1), (x,line_id-1)])
        number_neighbors.append([value, neighbor_coords])
    return number_neighbors

def get_symbol_coords(data, regex_string):
    # create a lookup of all symbol coordinates
    coords_map = defaultdict(lambda: defaultdict(bool))
    for idx, line in enumerate(data):
        for loc in get_symbol_locs_in_line(line, regex_string):
            coords_map[loc][idx] = True
    return coords_map
            
def get_number_map(data):
    number_map = []
    for idx, line in enumerate(data):
        number_map.extend(get_number_neighbors_in_line(line, idx))
    return number_map
        
            
def process_data(data):
    tot = 0
    symbol_map = get_symbol_coords(data, PART_1_REGEX)
    number_map = get_number_map(data)
    # check each number neighbor coordinate set to see if exists in symbol map
    for n in number_map:
        for coord in n[1]:
            x = coord[0]
            y = coord[1]
            if symbol_map[x][y]:
                tot += n[0]
                continue
    return tot

assert process_data(test_data) == 4361
part_1 = process_data(data) 


print(f"Part 1: {part_1}")

# part 2
def process_data_part_2(data):
    gear_ratio = 0
    possible_gears = defaultdict(lambda: defaultdict(list))
    symbol_map = get_symbol_coords(data, PART_2_REGEX)
    number_map = get_number_map(data)
    for n in number_map:
        for coord in n[1]:
            x = coord[0]
            y = coord[1]
            if symbol_map[x][y]:
                possible_gears[x][y].append(n[0])
                continue
    for item in possible_gears.values():
        for val in item.values():
            if len(val) == 2:
                gear_ratio += val[0] * val[1]
    return gear_ratio

assert process_data_part_2(test_data) == 467835
part_2 = process_data_part_2(data)

print(f"Part 2: {part_2}")