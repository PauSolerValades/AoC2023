with open('input.txt', 'r') as file:
    
    matrix = [
        [
            set(value for value in element.split(" ") if value != '') 
            for element in line[line.find(":")+2:].strip("\n").split("|")
        ]
        for line in file
    ]
    

counts = [(index, len(numbers.intersection(winning))) for index, (numbers, winning) in enumerate(matrix, start=1)]

number_of_games = {game: 1 for game in range(1, len(matrix) + 1)}

for game, repetitions in counts:
    for i in range(1, repetitions + 1):
        number_of_games[game + i] = number_of_games.get(game + i, 1) + number_of_games[game]

result = sum(number_of_games.values())
print(result)