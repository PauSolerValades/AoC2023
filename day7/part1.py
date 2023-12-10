
EQ = {key: value for key, value in zip('J23456789TQK', 'MLKJIHGFEDCBA')}
QE = {value: key for key, value in zip('J23456789TJQK', 'MLKJIHGFEDCBA')}

"""
Punts de millora després de cotillejar solucions dels altres:
1. Els diccionaris per canviar de string 1 a string 2 són massa overkill. Pots
fer servir quelcom com:

trans_table = str.maketrans('J23456789TQKA', 'MLKJIHGFEDCBA')
translated_hand = hand.translate(trans_table)

que és super elegant. En essència,
str.maketrans fa una aplicació bijectiva element a element (J<->L, 2<->L)...
str.translate(str.maketrans) aplica l'aplicació a str, així no has de fer el panoli iterant
per diccionaris.

2. Lògica:
Retornar strings per posar-los a un diccionari i iterar per ells està bé, però pot ser millor.
Per exemple, la lògica de dins la funció evaluate hand només li fa falta mirar quants comptes, no fa falta
anar mirant lengths. És a dir, amb
[1,1,1,2] ja sap que només tens una parella
[1,4] només pot ser un poker
[3,2] només un full.

apart, tècnicament estàs comptant diverses vegades el mateix nombre quan crides a la funció auxiliar, cosa que no et fa falta.

T'has complicat una miqueta més del que feia falta.
Això sí, molt ben pensat que python t'ordenés la llista per si mateix, això és el que he trobat
més horrible de les altres implementacions
"""



with open('input.txt', 'r') as file:
    data = (line.strip("\n").split(" ") for line in file)
    data = {"".join([EQ.get(letter, letter) for letter in hand]): int(bid) for hand, bid in data}

def evaluate_hand(hand: str):

    letters_amount = {letter: hand.count(letter) for letter in set(hand)}

    if len(letters_amount.keys()) == len(hand):
        if EQ["J"] in letters_amount.keys():
            grade = "pair"
        else:
            grade = "high"
    
    # es repeteix només una lletra => només un duo
    elif len(letters_amount.keys()) == len(hand)-1:
        if letters_amount.get(EQ['J'], 0) == 0:
            grade = "pair"
        else:
            grade = "trio"

    # hi ha tres lletres i dues repetides => dos dobles
    elif len(letters_amount.keys()) == len(hand)-2 and len(find_letter_repeated(2, letters_amount)) == 2:
        if letters_amount.get(EQ['J'], 0) == 0:
            grade= "twopair"
        elif letters_amount.get(EQ['J'], 0) == 1:
            grade = "full"
        else:
            grade = "four"

    # hi ha tres lletres i una tres vegades => un trio
    elif len(letters_amount.keys()) == len(hand)-2 and len(find_letter_repeated(3, letters_amount)) == 1:
        if letters_amount.get(EQ['J'], 0) == 0:
            grade= "trio"
        else:
            grade = "four"

     # hi ha dues lletres, una repetida quatre cops => poker
    elif len(letters_amount.keys()) == len(hand)-3 and len(find_letter_repeated(4, letters_amount)) == 1:
        if letters_amount.get(EQ['J'], 0) == 0:
            grade= "four"
        else:
            grade = "five"

    # hi ha dues lletres, una repetida tres cops i una dos => full house
    elif len(letters_amount.keys()) == len(hand)-3:
        if letters_amount.get(EQ['J'], 0) == 0:
            grade= "full"
        else:
            grade = "five"

    # hi ha una lletra => super
    elif len(letters_amount.keys()) == len(hand)-4:
        grade = "five"
    else:
        print("Number non accounted...")
        grade = "none"

    #print(f"Hand {hand}: value = {list(value)}, sum = {sum(value)}")
    return grade

def find_letter_repeated(repetitions: list, dictionary: dict):
    return [letter for letter, amount in dictionary.items() if repetitions == amount]

# now we classify it for the grade they have:
classification = {grade: [] for grade in ["high", "pair", "twopair", "trio", "full", "four", "five"]}
evaluated_hands = [(evaluate_hand(hand), hand) for hand in data.keys()]

for grade, hand in evaluated_hands:
    classification[grade] += [hand]

sorted_list = [element for grades in classification.values() for element in sorted(grades, reverse=True)]
print(["".join([QE.get(letter, letter) for letter in element]) for element in sorted_list])
result = sum((index*data[hand] for index, hand in enumerate(sorted_list, start=1)))
print(result)
