from random import randrange

def create_card():
    new_card = {}
    count = 1
    num = 15

    for key in ('B', 'I', 'N', 'G', 'O'):
        list = []
        for i in range(5):
            list.append(randrange(count, count+num))
        new_card[key] = list
        count = count + num

    return new_card

def print_card(card):
    for item in card.items():
        print(item[0])
        for num in item[1]:
            print(num)
        print()

print_card(create_card())