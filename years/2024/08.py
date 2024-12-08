# day 8
from years.process import get_response
from collections import defaultdict

test_input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

response = get_response(day=8, year=2024)

def get_antinodes_part_1(node, other_nodes, lim_i, lim_j):
    antinodes = set()
    for point in other_nodes:
        if point != node:
            delta_x = node[0] - point[0]
            delta_y = node[1] - point[1]
            an_x = node[0] + delta_x
            an_y = node[1] + delta_y
            if 0 <= an_x < lim_i and 0 <= an_y < lim_j:
                antinodes.add((an_x, an_y))
    return antinodes


def build_matrix(data):
    lines = data.strip().split("\n")
    lim_j = len(lines)
    lim_i = len(lines[0])
    matrix = defaultdict(list)
    for j, line in enumerate(lines):
        for i, symbol in enumerate(line):
            if symbol != ".":
                matrix[symbol].append((i,j))
    return matrix, lim_i, lim_j

def part_1(data):
    matrix, lim_i, lim_j = build_matrix(data)
    antinodes = set()
    for coords in matrix.values():
        for coord in coords:
            antinodes.update(get_antinodes_part_1(coord, coords, lim_i, lim_j))
    return len(antinodes)

assert part_1(test_input) == 14
print(f"Part 1 = {part_1(response)}")

def get_antinodes_part_2(node, other_nodes, lim_i, lim_j):
    antinodes = set()
    for point in other_nodes:
        an_x = node[0]
        an_y = node[1]
        if point != node:
            delta_x = node[0] - point[0]
            delta_y = node[1] - point[1]
            antinodes.add((an_x, an_y))
            while 0 <= an_x < lim_i or 0 <= an_y < lim_j:
                an_x += delta_x
                an_y += delta_y
                if 0 <= an_x < lim_i and 0 <= an_y < lim_j:
                    antinodes.add((an_x, an_y))
    return antinodes

def part_2(data):
    matrix, lim_i, lim_j = build_matrix(data)
    antinodes = set()
    for coords in matrix.values():
        for coord in coords:
            antinodes.update(get_antinodes_part_2(coord, coords, lim_i, lim_j))
    return len(antinodes)

assert part_2(test_input) == 34
print(f"Part 2 = {part_2(response)}")