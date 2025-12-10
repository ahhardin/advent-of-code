from years.process import *
from shapely import Polygon

test_input = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
real_input = get_response(day=9, year=2025)

def process_input_into_coords(input_data):
    return [tuple((int(line)) for line in di.split(",")) for di in input_data.strip().split("\n")]

def get_all_rectangles(coords):
    rectangles = {}
    for x1, y1 in coords:
        for x2, y2 in coords:
            if (x1, y1) == (x2, y2) or frozenset([(x1,y1),(x2,y2)]) in rectangles:
                continue
            key = frozenset([(x1,y1), (x2,y2)])
            rectangles[key] = (abs(x1-x2)+1)*(abs(y1-y2)+1)
    return sorted([(v, k) for k,v in rectangles.items()], key=lambda x: x[0], reverse=True)

def part_1(input_data):
    sorted_rectangles = get_all_rectangles(process_input_into_coords(input_data))
    return sorted_rectangles[0][0]

assert part_1(test_input) == 50
with timer() as t:
    print(f"Part 1: {part_1(real_input)}")

print(f"time elapsed {t()}s")

def build_matrix(coords):  
    return Polygon(coords)
    
def part_2(input_data):
    coords = process_input_into_coords(input_data)
    sorted_rectangles = get_all_rectangles(coords)
    matrix = build_matrix(coords)
    for area, (p1,p2) in sorted_rectangles:
        polygon = Polygon([p1, (p1[0], p2[1]), p2, (p2[0], p1[1])])
        if polygon.within(matrix):
            return area

assert part_2(test_input) == 24
with timer() as t:
    print(f"Part 1: {part_2(real_input)}")

print(f"time elapsed {t()}s")