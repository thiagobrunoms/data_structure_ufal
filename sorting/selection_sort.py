def selection_sort(elements: list):
    size = len(elements)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if elements[j] < elements[min_index]:
                min_index = j

        elements[i], elements[min_index] = elements[min_index], elements[i]

    return elements

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)