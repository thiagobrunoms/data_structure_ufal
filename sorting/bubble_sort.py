#https://www.youtube.com/watch?v=lyZQPjUT5B4
def bubble_sort(elements: list):
    n = len(elements)
    for i in range(n):
        #Últimos i's já foram ordenados
        for j in range(n - i - 1):
            if (elements[j] > elements[j+1]):
                elements[j], elements[j+1] = elements[j+1], elements[j]

    return elements


numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
