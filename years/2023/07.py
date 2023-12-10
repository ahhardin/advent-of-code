# day 7
from years.process import get_response, parse_response_to_array
raw_test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
test_data = [{"cards": d[:5], "bet": int(d[6:])} for d in parse_response_to_array(raw_test_data)]

def process_data(data):
    return [{"cards": d[:5], "bet": int(d[6:])} for d in parse_response_to_array(data)]

data = process_data(get_response(day=7))

from collections import Counter
face_card_mapping = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}

def get_card_strength(card):
    try:
        return int(card)
    except:
        return face_card_mapping[card]

def get_strength(hand):
    if "replaced" in hand:
        counts = Counter(hand["replaced"]).values()
    else:
        counts = Counter(hand["cards"]).values()
    hand["score"] = 0
    if 5 in counts:
        hand["score"] = 6
    elif 4 in counts:
        hand["score"] = 5
    elif 3 in counts:
        if 2 in counts:
            hand["score"] = 4
        else:
            hand["score"] = 3
    elif 2 in counts:
        if len(counts) == 3:
            hand["score"] = 2
        else:
            hand["score"] = 1
    return hand
    

def rank_hands(hands):
    for hand in hands:
        get_strength(hand)
    return sorted(hands, key=lambda h: (
        -h["score"], 
        -get_card_strength(h["cards"][0]),
        -get_card_strength(h["cards"][1]),
        -get_card_strength(h["cards"][2]),
        -get_card_strength(h["cards"][3]),
        -get_card_strength(h["cards"][4]),
    ))

def part_1(hands):
    ranking = rank_hands(hands)
    total = 0
    for idx, r in enumerate(reversed(ranking)):
        total += (idx+1)*r["bet"]
    return total

assert part_1(test_data) == 6440
part_1 = part_1(data) # 253205868

print(f"Part 1: {part_1}")

# part 2
face_card_mapping_2 = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
}

def get_card_strength_2(card):
    try:
        return int(card)
    except:
        return face_card_mapping_2[card]

def get_strength_with_jokers(hand):
    counter = Counter(hand["cards"])
    counts = counter.values()
    hand["score"] = 0
    hand["replaced"] = hand["cards"]
    num_jokers = 0
    if "J" in counter:
        num_jokers = counter["J"]
        # add num jokers to the highest counter and then use part_1 method
        sorted_counter = sorted(counter.items(), key=lambda c: -c[1])
        most_frequent = sorted_counter[0][0]
        if most_frequent == "J":
            if sorted_counter[0][1] == 5:
                most_frequent = "A"
            else:
                most_frequent = sorted_counter[1][0]
        hand["replaced"] = hand["cards"].replace("J", most_frequent)
    return get_strength(hand)
    
    
def rank_hands_2(hands):
    for hand in hands:
        get_strength_with_jokers(hand)
    return sorted(hands, key=lambda h: (
        -h["score"], 
        -get_card_strength_2(h["cards"][0]),
        -get_card_strength_2(h["cards"][1]),
        -get_card_strength_2(h["cards"][2]),
        -get_card_strength_2(h["cards"][3]),
        -get_card_strength_2(h["cards"][4]),
    ))

def part_2(hands):
    ranking = rank_hands_2(hands)
    total = 0
    for idx, r in enumerate(reversed(ranking)):
        total += (idx+1)*r["bet"]
    return total

assert part_2(test_data) == 5905
part_2 = part_2(data) # 253907829

print(f"Part 2: {part_2}")