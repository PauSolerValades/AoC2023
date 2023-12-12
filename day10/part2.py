from itertools import groupby
import numpy as np
import sys
sys.setrecursionlimit(10000)
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

while True:
    
    actual_coord = next_position(entry, actual_coord, matrix[actual_coord[0]][actual_coord[1]])
    entry = path[-1]
    if actual_coord == s:
        break
    path.append(actual_coord)

def remove_next_except_jump(sublist):
    if not sublist:
        return []

    # Start with the first tuple
    result = [sublist[0]]

    for i in range(1, len(sublist)):
        # Check if non-contiguous with the previous one
        if sublist[i][1] != sublist[i-1][1] + 1:
            # Add the last of the contiguous segment
            if result[-1] != sublist[i-1]:
                result.append(sublist[i-1])
            # Start a new segment
            result.append(sublist[i])

    # Add the last element if it's not already in the result
    if result[-1] != sublist[-1]:
        result.append(sublist[-1])

    return result
            

def flood_fill(matrix, x, y, path, marked):
    """
    Flood fill algorithm to mark all points reachable from (x, y) that are not part of the path.
    """
    if (x, y) in path or (x, y) in marked:
        return

    # Mark the current point
    marked.add((x, y))

    # Directions: up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check bounds
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
            flood_fill(matrix, nx, ny, path, marked)

def count_inside_points(matrix, path):
    """
    Count the number of points inside the path using the flood fill algorithm.
    """
    marked = set()
    # Start flood fill from the top-left corner (0, 0)
    flood_fill(matrix, 0, 0, set(path), marked)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i,j) in path:
                continue
            if (0,j) not in marked:
                flood_fill(matrix, 0, j, set(path), marked)
            if (i,0) not in marked:
                flood_fill(matrix, i, 0, set(path), marked)
            if (len(matrix)-1, j) not in marked:
                flood_fill(matrix, len(matrix), j, set(path), marked)
            if (i, len(matrix[0])-1) not in marked:
                flood_fill(matrix, i, len(matrix[0])-1, set(path), marked)




    # Count points not marked by flood fill
    with open('output.txt', 'w') as file:
                
        inside_points = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in path and (i, j) not in marked:
                    inside_points += 1
                    file.write('*')
                else:
                    file.write('.')
            file.write('\n')
        

    return inside_points

# Counting the inside points using flood fill
inside_points_count = count_inside_points(matrix, path)
print(inside_points_count)

marked = set()
flood_fill(matrix, 71,72, path, marked)
print(len(marked))



"""
path.sort(key=lambda x: x[0])
def group_path_into_segments(path):
    # Sorting path to start from the top-left and move right, then down
    path.sort(key=lambda x: (x[0], x[1]))

    # Grouping path points into segments
    segments = []
    current_segment = [path[0]]

    for i in range(1, len(path)):
        # Check if current point is a continuation of the segment
        if (path[i][0] == path[i-1][0] and path[i][1] == path[i-1][1] + 1) or \
           (path[i][1] == path[i-1][1] and path[i][0] == path[i-1][0] + 1):
            current_segment.append(path[i])
        else:
            segments.append(current_segment)
            current_segment = [path[i]]
    segments.append(current_segment)

    return segments

def is_in_some_segment(tup, list_of_lists):
    for i, l in enumerate(list_of_lists):
        if tup in l:
            
            return i
    return -1

segmented_path = group_path_into_segments(path)
points_in = 0
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        # trace the beam
        if is_in_some_segment((i,j), segmented_path) != -1:
            continue

        crossings = 0
        for b in range(j,len(row)):
            if (num_f := is_in_some_segment((i,b), segmented_path)) != -1:
                if (num_s := is_in_some_segment((i,b+1), segmented_path)) != num_f:
                    crossings +=1
                
        if crossings%2==1: points_in+=1
"""
