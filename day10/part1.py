def find_s_coords(matrix: list[str]):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 'S':
                return (i,j)     

def deduce_flow(up: str, down: str, left: str, right: str) -> tuple[int, int]:
    down_can = 'LJ|'
    up_can = '7F|'
    left_can = 'LF-'
    right_can = 'J-7'
    candidates = {
        '-': {'left': left_can, 'right': right_can},
        '|': {'up': up_can, 'down': down_can},
        'L': {'up': up_can, 'right': right_can},
        'F': {'down': down_can, 'right': right_can},
        'J': {'up': up_can, 'left': left_can},
        '7': {'left': left_can, 'down': down_can}
    }

    options = []
    for key, directions in candidates.items():
        accomplished = (
            up in directions.get('up', '_'),
            down in directions.get('down', '_'),
            left in directions.get('left', '_'),
            right in directions.get('right', '_')
        )
        print(f"Accomplished: {accomplished} for char {key}")
        if sum((1 for accomplish in accomplished if accomplish == True)) == 2:
            options.append(key)
        
    return options


def move(coord: tuple[int, int], direction: str) -> tuple[int, int]:
    x,y = coord[0], coord[1]

    match(direction):
        case 'u':
            return (x-1,y)
        case 'd':
            return (x+1,y)
        case 'l':
            return (x,y-1)
        case 'r':
            return (x,y+1)
        case _:
            return (-1,-1)
        
def flux_direction(last: tuple[int, int], actual: tuple[int,int]) -> str:
    diff = tuple(map(lambda x, y: x - y, actual, last))

    if diff == (1,0):
        return 'u'
    elif diff == (-1,0):
        return 'd'
    elif diff == (0,1):
        return 'l'
    else:
        return 'r'
        
def next_position(entry: tuple[int, int], actual: tuple[int,int], letter: str):

    flux_enters = flux_direction(entry, actual)

    match(letter):
        case '-':
            next_position = 'r' if flux_enters=='l' else 'l'
        case '|':
            next_position = 'd' if flux_enters=='u' else 'u'
        case 'F':
            next_position = 'd' if flux_enters=='r' else 'r'
        case 'L':
            next_position = 'u' if flux_enters=='r' else 'r'
        case 'J':
            next_position = 'l' if flux_enters=='u' else 'u'
        case '7':
            next_position = 'l' if flux_enters=='d' else 'd'

    return move(actual, next_position)    
            

with open("input.txt", 'r') as file:
    matrix = [line.strip("\n") for line in file]

s = find_s_coords(matrix)
coords = {
    direction: ((c := move(s, direction)), matrix[c[0]][c[1]]) 
    for direction in ['u','d','l','r']
}
chars = deduce_flow(coords['u'][1], coords['d'][1], coords['l'][1], coords['r'][1])

print(f"S found! Inerpolated a {chars} as S!")
#assumim que chars == 1
char = chars[0]

possible_directions = {
    '-': ['l','r'],
    '|': ['u','d'],
    'L': ['u', 'r'],
    'F': ['d', 'r'],
    'J': ['u', 'l'],
    '7': ['d', 'l']
}
print(f"Chosen Loop direction: {possible_directions[char][0]}")
path = [s, actual_coord := next_position(move(s, possible_directions[char][0]), s, char)]
entry = s

print(path)
while True:
    
    actual_coord = next_position(entry, actual_coord, matrix[actual_coord[0]][actual_coord[1]])
    entry = path[-1]
    if actual_coord == s:
        break
    path.append(actual_coord)
    
print(path)
result = int(round(len(path)/2,0))

print(result)



