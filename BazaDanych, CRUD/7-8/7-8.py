cats = 'cats.txt'
dogs = 'dogs.txt'

try:
    with open(cats, encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Plik cats.txt nie istnieje")

try:
    with open(dogs, encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    #print("Plik dogs.txt nie istnieje") # Niepowodzenie z obsługą
    pass # "Ciche" niepowodzenie