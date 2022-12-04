## day 4 ##
import requests
import re
from secrets import SESSION
response = requests.get('https://adventofcode.com/2022/day/4/input', headers={'Cookie': SESSION})
data = response.content.decode('utf-8').strip().split('\n')
full_overlaps = 0
partial_overlaps = 0
for d in data:
    matches = re.search("(?P<e1a>[0-9]+)-(?P<e1b>[0-9]+),(?P<e2a>[0-9]+)-(?P<e2b>[[0-9]+)", d)
    e1a = int(matches.group('e1a'))
    e1b = int(matches.group('e1b'))
    e2a = int(matches.group('e2a'))
    e2b = int(matches.group('e2b'))
    if (e1a >= e2a and e1b <= e2b) or (e2a >= e1a and e2b <= e1b):
        full_overlaps += 1
    elif (e1a >= e2a and e1a <= e2b) or (e1b <= e2b and e1a >= e2a) or (e2a >= e1a and e2a <= e1b) or (e2b <= e1b and e2b >= e1a):
        partial_overlaps += 1
    
print(f"full overlaps: {full_overlaps}")
print(f"all_overlaps: {full_overlaps + partial_overlaps}")