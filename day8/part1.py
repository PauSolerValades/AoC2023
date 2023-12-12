with open('input.txt', 'r') as file:
    rl_sequence = file.readline().strip().strip("\n")
    file.readline() #skip empty line

    data = {key.strip(): tuple(value.strip().strip('()').split(', ')) 
        for line in file 
        for key, value in [line.strip().split(' = ')]}

# we convert left and right into zeros and ones to enter the list faster
binaryRL = rl_sequence.translate(str.maketrans("LR", "01"))
actual_point = 'AAA' #starting point
i=0
mod = len(binaryRL)
iterations = 0

while actual_point != 'ZZZ':

    actual_point = data[actual_point][int(binaryRL[i])]
    
    i = (i+1)%mod
    iterations += 1

print(iterations)