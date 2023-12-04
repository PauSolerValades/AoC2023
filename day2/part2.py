from math import prod

def process_line(line: str) -> dict:
    samples = line.strip().split(':')[1].split(';')
    return [{color_split[1]: int(color_split[0]) 
             for color_split in [color.strip().split(' ') for color in sample.split(',')] }
            for sample in samples]


with open('input.txt', 'r') as file:
    processed_games = [process_line(line) for line in file]


def minimum_colours_possible(game) -> tuple[int, int, int]:
    max_blue = max(s.get("blue", 0) for s in game)
    max_red = max(s.get("red", 0) for s in game)
    max_green = max(s.get("green", 0) for s in game)

    return max_green, max_red, max_blue

total = sum(prod(minimum_colours_possible(game)) for game in processed_games)
print(total)
