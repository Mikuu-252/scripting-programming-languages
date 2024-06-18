word = "Zdanie do zaszyfrowania"
dis = 3
end = False

while not end:
    option = input("Wybierz opcje z menu: \n1. Szyfrator\n2. Deszyfrator\n3. Koniec")
    
    if option == "1":
        new_word = ""
        for char in word:
            char = ord(char)
            if char == ord(" "):
                new_word += chr(char)
                continue

            for i in range(dis):
                if char == ord('z'):
                    char = ord('a')
                    continue
                elif char == ord('Z'):
                    char = ord('A')
                    continue
                
                char = char + 1
            
            new_word += chr(char)
        print(new_word)

    elif option == "2":
        new_word = ""
        for char in word:
            char = ord(char)
            if char == ord(" "):
                new_word += chr(char)
                continue

            for i in range(dis):
                if char == ord('a'):
                    char = ord('z')
                    continue
                elif char == ord('A'):
                    char = ord('Z')
                    continue
                
                char = char - 1
            
            new_word += chr(char)
        print(new_word)
    elif option == "3":
        end = True
    else:
        print("Wybierz poprawna opcje")


