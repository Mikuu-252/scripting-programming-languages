f = open("test.txt", 'r')

word = f.readline()

if len(word) > 3:
    crypt_word = "#"
    count = 0
    for char in word:
        crypt_word += str(count)
        crypt_word += char
        count += 1
    crypt_word += str(count)
    crypt_word += "#"

    e_f = open("crypted_test.txt", 'w')
    e_f.write(crypt_word)
else:
    print("Słowo jest za krótkie")