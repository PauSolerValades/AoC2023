import re
from math import prod

with open('input.txt', 'r') as file:
    matrix = {
        (row, column): symbol 
        for row, line in enumerate(file, start=1) 
        for column, symbol in enumerate(line, start=1) 
        if symbol not in [".", "\n"]
    }

    file.seek(0) #reseteja el cursor de lectura

    numbers = {
        (row, i): int(match.group())
        for row, line in enumerate(file, start=1)
        for match in re.finditer(r'\d+', line)
        for i in range(match.start()+1, match.end()+1)
    }    
    

# busquem els punts que només siguin *
symbols = [key for key, value in matrix.items() if value == "*"]

def adjacent_numbers(position: tuple[int, int], matrix: dict) -> list[tuple[int, int]]:
    """
    Torna les posicions adjacents que estan a la matriu (no els punts, només els nombres)
    """
    return [
        (position[0]+i,position[1]+j) 
        for i in range(-1,2) for j in range(-1,2) 
        if not (i,j) == (0,0) and (position[0]+i,position[1]+j) in matrix
    ]

# ens guardem en un diccionari els adjaçents de ada asterisc
adjacent_numbers_to_asterics = {position: adjacent_numbers(position, matrix) for position in symbols}
print(adjacent_numbers_to_asterics)

def eliminate_consecutive(positions):
    consecutives = {(x, y + 1) for x, y in positions if (x, y + 1) in positions}
    return list(set(positions) - consecutives)

# eliminem les posicions consecutives dels nombres.
last_positions = {key: eliminate_consecutive(value) for key, value in adjacent_numbers_to_asterics.items()}
keys_with_no_gears = [key for key, value in last_positions.items() if len(value) < 2]

# eliminem els asteriscs que no tenen dos elements!
for key in keys_with_no_gears:
    last_positions.pop(key)


result = sum([prod([numbers[position] for position in value]) for value in last_positions.values()])
print(result)
"""
Idea: crear un diccionari que tingui key: posició, value: què hi ha. La idea és no haver de carregar els punts i buits a memoria
un cop fet, fer una funció que, donada una posició, entri a les adjaçents (fer-ho amb get per no haver-se de preocupar dels costats!)
"""