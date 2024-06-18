word_to_guess = "Robak"
word_to_guess = word_to_guess.upper()
lives = 10

player_answer = []
word_disp = []


for char in word_to_guess:
    word_disp.append("_")

end = False

while not end:
    print("Słowo które zgadujesz:")
    print(word_disp)
    print("\n Litery które wpisałeś:")
    print(player_answer)
    print(f"\n Liczba pozostałych prób {lives}")

    player_char = ''
    player_char = input("Wprowadz litere:")
    player_char = player_char.upper()

    if player_char in player_answer:
        print("Podales juz te litere")
        continue

    if player_char in word_to_guess:
        index = 0
        for char in word_to_guess:
            if char == player_char:
                word_disp[index] = char
            index += 1
        player_answer.append(player_char)
    else:
        player_answer.append(player_char)
        lives -= 1

    if lives == 0:
        print("Koniec zyc przegrales")
        end = True
    if not('_' in word_disp):
        print("Wygrales gratulacje")
        end = True