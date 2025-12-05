from years.process import *

real_data_raw = (get_response(day=4, year=2025))
test_data_raw = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
def process_data(raw_data):
    return parse_response_to_array(raw_data.strip())
  
test_data = process_data(test_data_raw)
real_data = process_data(real_data_raw)

def process_line_into_matrix(line, row_num, matrix):
    for idx, item in enumerate(line):
        if item == "@":
            matrix[(idx, row_num)] = False # can it be removed
    return matrix

def build_matrix(data):
    matrix = {}
    for idx, line in enumerate(data):
        matrix = process_line_into_matrix(line, idx, matrix)
    return matrix, idx

def get_displacements():
    return [(i,j) for i in range(-1,2) for j in range(-1,2) if (i,j) != (0,0)]

def check_surrounding_spots(x, y, matrix, limit):
    count = 0
    for i, j in get_displacements():
        new_x = x+i
        new_y = y+j
        if 0 <= new_x <= limit and 0 <= new_y <= limit and matrix.get((new_x, new_y)) is not None:
            count += 1
    return count
    
        
def part_1(data):
    matrix, idx = build_matrix(data)
    num_accessible = 0
    for i, j in matrix.keys():
        num_surrounding = check_surrounding_spots(i, j, matrix, idx)
        if num_surrounding < 4:
            num_accessible += 1
    return num_accessible

assert part_1(test_data) == 13
print(f"Part 1: {part_1(real_data)}")


def remove_rolls(matrix, num_removed, limit):
    removed_in_iteration = 0
    for i, j in matrix.keys():
        num_surrounding = check_surrounding_spots(i, j, matrix, limit)
        if num_surrounding < 4:
            matrix[(i,j)] = True
            num_removed += 1
            removed_in_iteration += 1
    matrix = {(key[0], key[1]): False for key in matrix.keys() if not matrix[key]}
    if removed_in_iteration > 0:
        return remove_rolls(matrix, num_removed, limit)
    return num_removed

def part_2(data):
    matrix, idx = build_matrix(data)
    num_removed = remove_rolls(matrix, 0, idx)
    
    return num_removed


assert part_2(test_data) == 43
print(f"Part 2: {part_2(real_data)}")