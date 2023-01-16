import requests
import re
from collections import defaultdict

from years.session import SESSION

test_input = "498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9"
pattern = "((\d+),(\d+))"
test_data = [[(int(r[1]), int(r[2])) for r in re.findall(pattern, text)] for text in test_input.split('\n')]

response = requests.get('https://adventofcode.com/2022/day/14/input', headers={'Cookie': SESSION})
real_input = response.content.decode('utf-8').strip()
real_data = [[(int(r[1]), int(r[2])) for r in re.findall(pattern, text)] for text in real_input.split('\n')]

def place_rocks(pt_a, pt_b):
    coords = {(pt_a): "#", (pt_b): "#"}
    dx = abs(pt_a[0] - pt_b[0])
    dy = abs(pt_a[1] - pt_b[1])
    min_x = min(pt_a[0], pt_b[0])
    min_y = min(pt_a[1], pt_b[1])
    for i in range(0, dx + 1):
        coords[(min_x + i, min_y)] = "#"
    for j in range(0, dy + 1):
        coords[(min_x, min_y + j)] = "#"
    return coords

def build_grid(data):
    grid = defaultdict(str)
    for row in data:
        for idx in range(0, len(row) - 1):
            grid.update(place_rocks(row[idx], row[idx + 1]))       
    return grid

def get_abyss_level(grid):
    return max([p[1] for p in grid.keys()]) + 1

def drop_sand_pt_1(grid):
    abyss_level = get_abyss_level(grid)
    # down, left diag, right diag
    step_order = [(0, 1), (-1, 1), (1, 1)]
    sand_number = 0
    step_down = lambda pt,step: tuple(map(lambda i, j: i + j, pt, step))
    at_abyss = False
    while not at_abyss:
        point = (500, 0)
        while True:
            if grid[step_down(point, step_order[0])]:
                # check left
                if grid[step_down(point, step_order[1])]:
                    # check right
                    if grid[step_down(point, step_order[2])]:
                        grid[point] = "o"
                        sand_number += 1
                        break
                    else:
                        point = step_down(point, step_order[2])
                else:
                    point = step_down(point, step_order[1])
            else:
                point = step_down(point, step_order[0])
            if point[1] > abyss_level:
                at_abyss = True
                break
    return sand_number
                        
        
assert(drop_sand_pt_1(build_grid(test_data)) == 24)
print(f"part 1: {drop_sand_pt_1(build_grid(real_data))}")

def drop_sand_pt_2(grid):
    floor_level = get_abyss_level(grid)
    # down, left diag, right diag
    step_order = [(0, 1), (-1, 1), (1, 1)]
    sand_number = 0
    step_down = lambda pt,step: tuple(map(lambda i, j: i + j, pt, step))
    blocked = False
    starting_point = (500, 0)
    while not blocked:
        point = starting_point
        while True:
            if grid[starting_point]:
                blocked = True
                break
            if grid[step_down(point, step_order[0])]:
                # check left
                if grid[step_down(point, step_order[1])]:
                    # check right
                    if grid[step_down(point, step_order[2])]:
                        grid[point] = "o"
                        sand_number += 1
                        break
                    else:
                        point = step_down(point, step_order[2])
                else:
                    point = step_down(point, step_order[1])
            else:
                point = step_down(point, step_order[0])
            if point[1] == floor_level:
                grid[point] = "o"
                sand_number += 1
                break
    return sand_number

assert(drop_sand_pt_2(build_grid(test_data)) == 93)
print(f"part 2: {drop_sand_pt_2(build_grid(real_data))}")