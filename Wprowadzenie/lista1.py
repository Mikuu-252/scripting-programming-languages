user_input = input()
list = []
while int(user_input) != 0:
    list.append(int(user_input))
    user_input=input()

list.sort()

for key in list:
    print(key)
