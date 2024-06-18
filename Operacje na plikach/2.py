import os
import shutil

end = False
while not end:
    menu_opt = input("Jaką opcje chcesz wykonac 1. Skopiować 2. Przenieść 3.Usunąć 4.Koniec")

    if menu_opt == '1':
        source_path = input("Jaka jest adres źródłowy:")
        dest_path = input("Jaka jest adres docelowy:")

        shutil.copy(source_path, dest_path)


    elif menu_opt == '2':
        source_path = input("Jaka jest adres źródłowy:")
        dest_path = input("Jaka jest adres docelowy:")

        shutil.copy(source_path, dest_path)
        os.remove(source_path)

    elif menu_opt == '3':
        source_path = input("Jaka jest adres źródłowy:")

        os.remove(source_path)
    elif menu_opt == '4':
        end = True
    else:
        print("Nieprawidlowa opcja")
