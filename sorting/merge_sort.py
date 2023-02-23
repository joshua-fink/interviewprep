"""
MERGE SORT

Strengths: Fast, parallelizable
Weaknesses: Space

Complexity
    Worst case time: O(n lg n)
    Best case time: O(n lg n)
    Avg case time: O(n lg n)
    Space: O(n)
"""

data = [8, 3, 2, 7, 9, 4, 1]

print("ORIGINAL", data)

def merge_together(arr1, arr2):
    i = 0
    j = 0
    arr = []

    while (i < len(arr1) and j < len(arr2)):
        if (arr1[i] <= arr2[j]):
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    while (i < len(arr1)):
        arr.append(arr1[i])
        i += 1

    while (j < len(arr2)):
        arr.append(arr2[j])
        j += 1

    return arr

def merge_sort(arr):
    mid = int(len(arr)/2)

    if len(arr) <= 1:
        return arr

    elif len(arr) == 2:
        return merge_together(arr[0:mid], arr[mid:])

    else:
        arr1 = merge_sort(arr[0:mid])
        arr2 = merge_sort(arr[mid:])
        return merge_together(arr1, arr2)

print("SOLVED  ", merge_sort(data))