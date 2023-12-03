# day 2
import regex as re
from collections import defaultdict

from years.process import get_response, parse_response_to_array

raw_test_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

data = parse_response_to_array(get_response(day=2))
test_data = parse_response_to_array(raw_test_data)

# part 1
def build_color_dict(line):
    get_color_group = lambda item: re.search("([0-9]+) (red|green|blue)", item)
    color_dict = {}
    for item in line:
      color_group = get_color_group(item)
      color_dict[color_group.group(2)] = int(color_group.group(1))
    return color_dict

def parse_line(line):
    id_loc = re.search("(?<=Game )([0-9]+)", line)
    game_id = id_loc.group()
    rest = line[id_loc.end()+1:]
    return game_id, [build_color_dict(tuple(item.strip() for item in t.strip().split(","))) for t in rest.split(";")]

MAX_COLORS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_valid(trial):
    for k, v in trial.items():
        if v > MAX_COLORS[k]:
            return False
    return True

def is_game_valid(trials):
    for trial in trials:
      if not is_valid(trial):
        return False
    return True

def part_1(data):
    games = {parse_line(line)[0]: parse_line(line)[1] for line in data}
    tot = 0
    for game_id, trials in games.items():
        if is_game_valid(trials):
            tot += int(game_id)
    return tot

assert part_1(test_data) == 8
part_1 = part_1(data)

# part 2
def get_game_max(trials):
    max_colors = defaultdict(int)
    for trial in trials:
        for k,v in trial.items():
            if max_colors[k] < v:
                max_colors[k] = v
    return max_colors["red"] * max_colors["blue"] * max_colors["green"]

def part_2(data):
    games = {}
    tot = 0
    for line in data:
      parsed = parse_line(line)
      games[parsed[0]] = parsed[1]
    for trials in games.values():
        tot += get_game_max(trials)
    return tot

assert part_2(test_data) == 2286

part_2 = part_2(data)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")