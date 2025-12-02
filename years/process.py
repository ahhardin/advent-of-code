import requests

from years.session import SESSION

def get_response(*, day, year):
    response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={'Cookie': SESSION})
    return response.content.decode("utf-8").strip()

def parse_response_to_array(content):
    return content.split('\n')