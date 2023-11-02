"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    if not array:
        return []
    if len(array) == 1:
        return array
    c1, c2 = 0, len(array) - 1
    pivot = array[-1]
    while c1 < c2:
        if array[c1] > pivot:
            array[c2], array[c2 - 1] = array[c2 - 1], array[c2]
            c2 -= 1
            pivot = array[c2]
            if c2 - c1 > 0:
                array[c1], array[c2 + 1] = array[c2 + 1], array[c1]
        else:
            c1 += 1
    return quicksort(array[:c2]) + [pivot] + quicksort(array[c2+1:])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
