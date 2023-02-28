def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while(left <= right):
        middle =  (right + left) // 2

        if list[middle] == target:
            return middle
        elif target > list[middle]:
            left = middle + 1
        elif target < list[middle]:
            right = middle - 1

    return -1

my_list = [2, 33, 47, 59, 62, 79, 80, 93, 100]
index = binary_search(my_list, 93)
if (index >= 0):
    print('Elemento encontrado na posição!', index)
else:
    print('Elemento não encontrado!')
