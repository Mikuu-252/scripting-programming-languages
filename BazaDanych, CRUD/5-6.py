#5-6
while True:
    a = input('Podaj pierwszą cyfrę:')
    b = input('Podaj drugą cyfrę: (q = koniec)')

    if b=='q':
        break
    try:
        print(f'Wynik dodawania to: {int(a)+int(b)}')
    except ValueError:
        print('Jedna z cyfr jest niepoprawna')