with open('input.txt', 'r') as file:
    
    matrix = [
        [
            set(value for value in element.split(" ") if value != '') 
            for element in line[line.find(":")+2:].strip("\n").split("|")
        ]
        for line in file
    ]
    

counts = [(index, len(numbers.intersection(winning))) for index, (numbers, winning) in enumerate(matrix, start=1)]

updates = {game: 1 for game in range(1, len(matrix) + 1)}

for game, repetitions in counts:
    for i in range(1, repetitions + 1):
        updates[game + i] = updates.get(game + i, 1) + updates[game]

result = sum(updates.values())
print(result)