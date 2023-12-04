import regex as re
from years.process import get_response, parse_response_to_array

response = get_response(day=4)
data = parse_response_to_array(response)

raw_test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
data = parse_response_to_array(response)
test_data = parse_response_to_array(raw_test_data)

# part 1
PATTERN = "Card\s+(?P<card_id>\d+):\s+(?P<winning>(?:\d+\s*)+)\|\s+(?P<card_nums>(?:\d+\s*)+)"

def parse_card(card):
    match = re.search(PATTERN, card)
    return {
        "card_id": int(match.group("card_id")),
        "winning": set(int(num) for num in match.group("winning").split(" ") if num),
        "card_nums": set(int(num) for num in match.group("card_nums").split(" ") if num)
    }

def get_num_wins(card_data):
    return len(card_data["winning"].intersection(card_data["card_nums"]))

def card_score(card):
    card_data = parse_card(card)
    num_wins = get_num_wins(card_data)
    return 2**(num_wins - 1) if num_wins else 0

def score_pile(data):
    return sum([card_score(card) for card in data])

assert score_pile(test_data) == 13
part_1 = score_pile(data) # 32609
print("Part 1:", part_1)

# part 2
def get_next_cards(card_data):
    num_wins = get_num_wins(card_data)
    return tuple(card_data["card_id"] + n for n in range(1, num_wins + 1))

def get_num_cards(data):
    cards_data = {}
    for card in data:
        card_data = parse_card(card)
        card_id = card_data["card_id"]
        cards_data[card_id] = card_data
        cards_data[card_id]["num"] = 1
        cards_data[card_id]["next_cards"] = get_next_cards(card_data)
    for card_data in cards_data.values():
        for _ in range(0, card_data["num"]):
            for new_card_id in card_data["next_cards"]:
                new_card = cards_data.get(new_card_id)
                if new_card:
                    cards_data[new_card_id]["num"] += 1
        
    return cards_data

assert sum([card["num"] for card in get_num_cards(test_data).values()]) == 30
part_2 = sum([card["num"] for card in get_num_cards(data).values()]) # 14624680
print("Part 2:", part_2)
