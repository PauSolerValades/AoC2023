import re

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
    

# busquem les parelles valors que no siguin nombres (simbols)
symbols = [key for key, value in matrix.items() if not value.isdigit()]

def adjacent_index(position: tuple[int, int]) -> list[tuple[int, int]]:
    return [(position[0]+i,position[1]+j) for i in range(-1,2) for j in range(-1,2) if not (i,j) == (0,0)]

all_adjacent_to_symbols = [adj_pos for position in symbols for adj_pos in adjacent_index(position)]
numbers_adjacent_to_symbols = [position for position in all_adjacent_to_symbols if position in matrix]

def eliminate_consecutive(positions):
    consecutives = {(x, y + 1) for x, y in positions if (x, y + 1) in positions}
    return list(set(positions) - consecutives)

last_positions = eliminate_consecutive(numbers_adjacent_to_symbols) #aquí només tenim una entrada per nombre

result = sum([numbers[position] for position in last_positions])
print(result)
"""
Idea: crear un diccionari que tingui key: posició, value: què hi ha. La idea és no haver de carregar els punts i buits a memoria
un cop fet, fer una funció que, donada una posició, entri a les adjaçents (fer-ho amb get per no haver-se de preocupar dels costats!)
"""