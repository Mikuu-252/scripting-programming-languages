user = [1, 12345678, 100]

end = False
while not end:
    menu_opt = input("Jaką opcje chcesz wykonac 1. Sprawdzic Saldo 2. Wykonac transakcje 3.Odczytac transajcje 4.Koniec")

    if menu_opt == '1':
        print(user[2])
    elif menu_opt == '2':
        amount = int(input("Wpisz kwote:"))
        operation_id = 0

        operation_content = f"Transakcja nr. {operation_id} \n Pesel: {user[1]} \n Saldo przed: {user[2]} \n Saldo po: {user[2]-amount} \n"
        user[2] -= amount
        print(operation_content)
        save = input("Zapisac do pliku? [y/n]")
        if save == 'y':
            f = open(f"tranzakcja_{operation_id}.txt",'w')
            f.write(operation_content)
            f.close
        operation_id += 1
    elif menu_opt == '3':
        operation_id = input('Wpisz numer transakcji:')

        f = open(f"tranzakcja_{operation_id}.txt",'r')
        for line in f.readlines():
            print(line, end='')
        f.close
    elif menu_opt == '4':
        end = True
    else:
        print("Nieprawidlowa opcja")
