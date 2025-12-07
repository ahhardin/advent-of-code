from years.process import *
from collections import defaultdict

test_input="""
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
real_input = get_response(day=7, year=2025)

def process_input(input_data):
    data = [d.strip() for d in input_data.strip().split("\n")]
    return data, len(data)

def build_matrix(data):
    matrix = {}
    starting_point = (0,0)
    for j, row in enumerate(data):
        for i, val in enumerate(row):
            if val == "^":
                matrix[(i,j)] = False # has it been hit
            if val == "S":
                starting_point = (i,j)
    return matrix, starting_point

def propagate_beam(positions, matrix):
    new_positions = set()
    for i,j in positions:
        j += 1
        if matrix.get((i,j)) is not None:
            new_positions.update([(i-1,j), (i+1,j)])
            matrix[i,j] = True
        else:
            new_positions.add((i,j))
    return new_positions, j

def part_1(input_data):
    data, size = process_input(input_data)
    matrix, starting_point = build_matrix(data)
    # start at starting point and move down until we hit a splitter
    new_positions, level = propagate_beam({starting_point}, matrix)
    while level < size - 1:
        new_positions, level = propagate_beam(new_positions, matrix)
    return sum(matrix.values())

assert part_1(test_input) == 21
print(f"Part 1: {part_1(real_input)}")

def propogate_beam_tachyon(positions, matrix, paths_traveled):
    new_positions = set()
    for i,j in positions:
        j += 1
        if matrix.get((i,j)) is not None:
            new_positions.update([(i-1,j), (i+1,j)])
            paths_traveled[i-1] += paths_traveled[i]
            paths_traveled[i+1] += paths_traveled[i]
            paths_traveled[i] = 0
        else:
            new_positions.add((i,j))
    return new_positions, j, paths_traveled
    

def part_2(input_data):
    data, size = process_input(input_data)
    matrix, starting_point = build_matrix(data)
    paths_traveled = defaultdict(int)
    paths_traveled[starting_point[0]] = 1
    new_positions, level, paths_traveled = propogate_beam_tachyon({starting_point}, matrix, paths_traveled)
    while level < size - 1:
        new_positions, level, paths_traveled = propogate_beam_tachyon(new_positions, matrix, paths_traveled)
    return sum(paths_traveled.values())
  
assert part_2(test_input) == 40
print(f"Part 2: {part_2(real_input)}")