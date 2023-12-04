def process_line(line: str) -> dict:
    samples = line.strip().split(':')[1].split(';')
    return [{color_split[1]: int(color_split[0]) 
             for color_split in [color.strip().split(' ') for color in sample.split(',')] }
            for sample in samples]

def is_possible(game: list[dict], max_reds: int, max_greens: int, max_blues: int):
    
    return all(
        [
            s.get("green", 0) <= max_greens and s.get("red", 0) <= max_reds and s.get("blue", 0) <= max_blues
            for s in game
        ]
    )


with open('input.txt', 'r') as file:
    processed_games = [process_line(line) for line in file]



result = sum(
    [index for index, game in enumerate(processed_games, start= 1) 
     if is_possible(game, max_reds=12, max_greens=13, max_blues=14)])
print(result)
    
    
