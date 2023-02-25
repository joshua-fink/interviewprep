"""
QUICKSORT

Strengths: Fast, parallelizable
Weaknesses: Slow worst case

Complexity
    Worst case time: O(n^2)
    Best case time: O(n lg n)
    Avg case time: O(n lg n)
    Space: O(lg n)
"""

data = [8, 1, 2, 7, 9, 3, 4]
print("ORIGINAL", data)

def partition(arr, start, end):
    
    left = start
    right = end - 1
    pivot = end

    while left <= right:

        while left <= end and arr[left] < arr[pivot]:
            left += 1
       
        while right >= start and arr[right] >= arr[pivot]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[left], arr[pivot] = arr[pivot], arr[left]

    if (left - start):
        arr = partition(arr, start, left - 1)

    if (end - left):
        arr = partition(arr, left + 1, end)
    
    return arr

def quicksort(arr):
    return partition(arr, 0, len(arr) - 1)

print("SOLVED  ", quicksort(data))
