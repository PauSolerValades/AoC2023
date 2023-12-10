from math import floor, ceil, sqrt
from time import time

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    info = [line.split(":")[1].strip("\n").replace(" ", "") for line in lines]

t, distance = int(info[0]), int(info[1])

t1 = time()
result = sum((1 for i in range(1,t) if i*(t-i) > distance))
t2 = time()

# amb una miqueta de manipulació és directe! (codi totalment copiat de reddit)
# osigui m'imaginava que això es podia fer però he preferit prvar primer força bruta hahahaha

t3 = time()
cota_superior = floor((t + sqrt(pow(t, 2) - 4 * distance))/2)
cota_inferior = ceil((t - sqrt(pow(t, 2) - 4 * distance))/2)
t4 = time()

print(f"Força bruta generadors {(t2-t1)}s. Quadràtic: {(t4-t3)}s")