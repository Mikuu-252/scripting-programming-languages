#1
learning_python = 'learning_python.txt'
content = ''
with open(learning_python, encoding='utf-8') as file:
    for line in file:
        content += line
    #for i in range(3):
        #print(content)

#2
guest_path = 'guest.txt'
guest = input('Podaj imie goscia:')

with open(guest_path, 'a+', encoding='utf-8') as file:
    file.write(guest)

#3
user_number = 4
count = 1
guest_book_path = 'guest_book.txt'

while count < user_number:
    guest = input('Podaj imie goscia:')

    with open(guest_book_path, 'a+', encoding='utf-8') as file:
        file.write(f'Użytkownik {guest} odwiedził strone\n')
    print(f'Witaj {guest}')
    count += 1

#4

answer_path = 'answers.txt'

while True:
    answer = input('Dlaczego lubisz programowac? (q = koniec)')

    if answer == 'q':
        break
    with open(answer_path, 'a+', encoding='utf-8') as file:
        file.write(f'{answer}\n')

