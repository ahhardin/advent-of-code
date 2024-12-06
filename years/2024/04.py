# day 3
import regex as re
from years.process import get_response

from collections import defaultdict

response = get_response(day=4, year=2024)

test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

test_data = test_input.strip().split("\n")
real_data = response.strip().split("\n")

def build_matrix(data):
    return {(i,j): letter for i, word in enumerate(data) for j, letter in enumerate(word)}

def build_text(data):
    lines = defaultdict(str)
    matrix = build_matrix(data)
    for (i,j), letter in matrix.items():
        lines[f"j{j}"] += letter
        lines[f"i{i}"] += letter
        lines[f"rd{i-j}"] += letter
        lines[f"ld{i+j}"] += letter

    return" ".join(lines.values())

def part_1(data):
    pattern = r"(?=(XMAS|SAMX))"
    text = build_text(data)
    return len(re.findall(pattern, text))

assert part_1(test_data) == 18
print(f"Part 1 = {part_1(real_data)}")


# part 2
comp = lambda x,y: tuple(x + y for x, y in zip(x, y))

def check_letter(matrix, idx):
    check_1 = [(-1, -1), (1, 1)]
    check_2 = [(1,-1), (-1, 1)]
    dr = {matrix.get(comp(idx, check_1[0])), matrix.get(comp(idx, check_1[1]))}
    dl = {matrix.get(comp(idx, check_2[0])), matrix.get(comp(idx, check_2[1]))}
    return dr == dl == {"M","S"}
        

def part_2(data):
    total = 0
    matrix = build_matrix(data)
    for idx, letter in matrix.items():
        if letter == "A":
            total += 1 if check_letter(matrix, idx) else 0
    return total

assert part_2(test_data) == 9
print(f"Part 2 = {part_2(real_data)}")