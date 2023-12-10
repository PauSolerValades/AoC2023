
from functools import reduce
from math import log

letter_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SORT_ORDER = {key: value for value, key in enumerate(letter_order, start=1)}
print(SORT_ORDER)
with open('input.txt', 'r') as file:
    data = (line.strip("\n").split(" ") for line in file)
    data = {"".join(sorted(hand, key=lambda x: SORT_ORDER[x])): int(bid) for hand, bid in data}
    #data = {hand: int(bid) for hand, bid in data}

def evaluate_hand(hand: str):

    letters_amount = {letter: hand.count(letter) for letter in set(hand)}
    base = 14

    if len(letters_amount.keys()) == len(hand):
        value = (SORT_ORDER[element] for element in letters_amount.keys())
    
    # es repeteix només una lletra => només un duo
    elif len(letters_amount.keys()) == len(hand)-1:
        pass
        repeated_letters = find_letter_repeated(2, letters_amount)
        value = (
            pow(base, 2) * SORT_ORDER[element] 
            if element in repeated_letters else SORT_ORDER[element] 
            for element in letters_amount.keys()
        )


    # hi ha tres lletres i dues repetides => dos dobles
    elif len(letters_amount.keys()) == len(hand)-2 and len(pairpair := find_letter_repeated(2, letters_amount)) == 2:
        pairpair = sorted(pairpair, key=lambda x: SORT_ORDER[x], reverse=True)
        missing_letter = reduce(lambda k, v: k if k not in pairpair else v, letters_amount) #només n'hi ha una no repetida
        value = (
            SORT_ORDER[element]*pow(base, index)
            for index, element in enumerate([missing_letter] + pairpair, start=0)
        )

    # hi ha tres lletres i una tres vegades => un trio
    elif len(letters_amount.keys()) == len(hand)-2 and len(trio := find_letter_repeated(3, letters_amount)) == 1:
        value = (
            pow(base, 3) * SORT_ORDER[element] 
            if element == trio[0] else SORT_ORDER[element] 
            for element in letters_amount.keys()
        )
     # hi ha dues lletres, una repetida quatre cops => poker
    elif len(letters_amount.keys()) == len(hand)-3 and len(quadra := find_letter_repeated(4, letters_amount)) == 1:
        value = (
            pow(base, 5) * SORT_ORDER[element] 
            if element == quadra[0] else SORT_ORDER[element] 
            for element in letters_amount.keys()
        )

    # hi ha dues lletres, una repetida tres cops i una dos => full house
    elif len(letters_amount.keys()) == len(hand)-3:
        print(sorted(letters_amount))
        value = (
            pow(base, index)*SORT_ORDER[element] #14**3 pel gran, 14**2 pel petit
            for index, element in enumerate(sorted(letters_amount, reverse=True), start=3)
        )

    # hi ha una lletra => super
    elif len(letters_amount.keys()) == len(hand)-4:
        value = (pow(base,6)*SORT_ORDER[element] for element in letters_amount)
    
    else:
        print("Number non accounted...")
        value = [-1]

    #print(f"Hand {hand}: value = {list(value)}, sum = {sum(value)}")
    p = sum(value)
    print(p)
    return log(p)


def find_letter_repeated(repetitions: list, dictionary: dict):
    return [letter for letter, amount in dictionary.items() if repetitions == amount]

sorted_hands = sorted([hand for hand in data.keys()], key=lambda x: evaluate_hand(x))
print(list(enumerate(sorted_hands, start=1)))
result = sum([data[hand]*index for index, hand in enumerate(sorted_hands, start=1)])
print(result)


