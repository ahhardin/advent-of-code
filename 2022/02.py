### day two ###
import requests
from secrets import SESSION

response = requests.get('https://adventofcode.com/2022/day/2/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n')
pairs = [p.split(' ') for p in data]
# part 1
def points(opp, you):
    mappings = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    opp_pts = mappings[opp]
    you_pts = mappings[you]
    if opp_pts == you_pts:
        return you_pts + 3
    if (opp_pts + 1) % 3 == you_pts % 3:
        return you_pts + 6
    return you_pts

total = 0
for p in pairs:
    total += points(p[0], p[1])
print(total)

# part 2
def points_pt_2(opp, result):
    mappings = {
        'A': 1,
        'B': 2,
        'C': 3,
    }
    opp_pts = mappings[opp]
    winner = lambda x: x % 3 + 1
    # loss
    if result == 'X':
        return winner(winner(opp_pts))
    # draw
    if result == 'Y':
        return opp_pts + 3
    # win
    if result == 'Z':
        return winner(opp_pts) + 6
    
total = 0
for p in pairs:
    total += points_pt_2(p[0], p[1])
print(total)