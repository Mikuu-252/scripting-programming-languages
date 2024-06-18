def remover(list, n):
    new_list = list
    new_list.sort()
    new_list = new_list[n:len(list)-n]
    return new_list

test_list = [1,2,3,4,5,6,7,8,9]
#test_list = [2, 3, 4, 5, 6, 0, -3, 4, -2, 90, 91]
#test_list = [0, 2, 3, 4, 4, 5, 6]

print(remover(test_list, 2))
