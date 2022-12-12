import requests
import re
import math
from functools import reduce
from collections import defaultdict

from years.session import SESSION

response = requests.get('https://adventofcode.com/2022/day/11/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n')
test_data = open('years/2022/11_test.txt').read().strip().split('\n')

def build_monkey_object(info):
    monkeys = defaultdict(lambda: {
        "items": [],
        "operation": None,
        "test": None,
        "true": None,
        "false": None,
        "inspections": 0
    })
    monkey = {}
    for idx, line in enumerate(info):
        if idx % 7 == 0:
            monkey_number = re.findall("\d+", line)[0]
            monkey = monkeys[monkey_number]
        elif idx % 7 == 1:
            monkey["items"] = [int(i) for i in re.findall("\d+", line)]
        elif idx % 7 == 2:
            monkey["operation"] = line.replace('old', 'x').replace("Operation: new = ", "")
        elif idx % 7 == 3:
            monkey["test"] = int(re.findall('\d+', line)[0])
        elif idx % 7 == 4:
            monkey["true"] = re.findall("\d+", line)[0]
        elif idx % 7 == 5:
            monkey["false"] = re.findall("\d+", line)[0]
    return monkeys


def process_monkey_business(info, rounds):
    monkeys = build_monkey_object(info)
    for r in range(0, rounds):
        for idx in list(monkeys.keys()).copy():
            m = monkeys[idx]
            for item in m["items"]:
                m["inspections"] += 1
                operation = lambda x: eval(m["operation"])
                item = operation(item)
                item = item // 3
                test = lambda x: x % m["test"] == 0
                if test(item):
                    monkeys[m["true"]]["items"].append(item)
                    m["items"] = m["items"][1:]
                else:
                    monkeys[m["false"]]["items"].append(item)
                    m["items"] = m["items"][1:]
    inspections = sorted([v["inspections"] for v in monkeys.values()], reverse=True)
    return inspections[0] * inspections[1]
    

assert(process_monkey_business(test_data, 20) == 10605)
print(f"part 1: {process_monkey_business(data, 20)}")

def process_monkey_business_pt2(info, rounds):
    monkeys = build_monkey_object(info)
    all_modulos = reduce((lambda x, y: x * y), [m["test"] for m in monkeys.values()])
    for r in range(0, rounds):
        for idx in list(monkeys.keys()).copy():
            m = monkeys[idx]
            for item in m["items"]:
                m["inspections"] += 1
                operation = lambda x: eval(m["operation"])
                item = operation(item)
                item = item % all_modulos
                test = lambda x: x % m["test"] == 0
                if test(item):
                    monkeys[m["true"]]["items"].append(item)
                    m["items"] = m["items"][1:]
                else:
                    monkeys[m["false"]]["items"].append(item)
                    m["items"] = m["items"][1:]
    inspections = sorted([v["inspections"] for v in monkeys.values()], reverse=True)
    return inspections[0] * inspections[1]

assert(process_monkey_business_pt2(test_data, 10000) == 2713310158)
print(f"part 2: {process_monkey_business_pt2(data, 10000)}")