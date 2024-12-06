# day 5
from years.process import get_response
from collections import defaultdict


test_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

response = get_response(day=5, year=2024)

def split_content(data):
    split_data = data.strip().split("\n\n")
    return [line.split("|") for line in split_data[0].split("\n")], [line.split(",") for line in split_data[1].split("\n")]

def build_rule_matrix(rules):
    rule_matrix = defaultdict(lambda: defaultdict(set))
    for rule in rules:
        rule_matrix[rule[0]]["after"].add(rule[1])
        rule_matrix[rule[1]]["before"].add(rule[0])
    return rule_matrix

def check_valid_line(line, rule_matrix):
    is_valid = True
    for idx, item in enumerate(line):
        rules = rule_matrix[item]
        before = set(line[:idx])
        after = set(line[idx+1:])
        if before.intersection(rules["after"]) or after.intersection(rules["before"]):
            is_valid = False
            break
    return is_valid

def get_valid_lines(lines, rule_matrix):
    valid_lines = []
    for line in lines:
        is_valid = check_valid_line(line, rule_matrix)
        if is_valid:
            valid_lines.append(line)
    return valid_lines

def part_1(data):
    rules, lines = split_content(data)
    rule_matrix = build_rule_matrix(rules)
    valid_lines = get_valid_lines(lines, rule_matrix)
    return sum([int(line[(len(line)//2)]) for line in valid_lines])
            

assert part_1(test_input) == 143
print(f"Part 1 = {part_1(response)}")

def reorder_invalid_line(line, rule_matrix):
    for idx, item in enumerate(line):
        rules = rule_matrix[item]
        before_wrong = set(line[:idx]).intersection(rules["after"])
        after_wrong = set(line[idx+1:]).intersection(rules["before"])
        if before_wrong:
            wrong_item = before_wrong.pop()
            wrong_index = line.index(wrong_item)
            line[idx] = wrong_item
            line[wrong_index] = item
        elif after_wrong:
            wrong_item = after_wrong.pop()
            wrong_index = line.index(wrong_item)
            line[idx] = wrong_item
            line[wrong_index] = item
    is_valid = check_valid_line(line, rule_matrix)
    if is_valid:
        return line
    else:
        return reorder_invalid_line(line, rule_matrix)

def part_2(data):
    newly_valid_lines = []
    rules, lines = split_content(data)
    rule_matrix = build_rule_matrix(rules)
    for line in lines:
        is_valid = check_valid_line(line, rule_matrix)
        if not is_valid:
            new_line = reorder_invalid_line(line, rule_matrix)
            newly_valid_lines.append(new_line)
    return sum([int(line[(len(line)//2)]) for line in newly_valid_lines])

assert part_2(test_input) == 123

print(f"Part 2 = {part_2(response)}")