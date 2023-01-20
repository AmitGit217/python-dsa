"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    arrLength = len(array)
    if arrLength <= 1:
        return array
    else:
        pivot = array.pop()
        lower = []
        greater = []

        for num in array:
            if num > pivot:
                greater.append(num)
            else:
                lower.append(num)
        
        return quicksort(lower) + [pivot] + quicksort(greater)


    



test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
