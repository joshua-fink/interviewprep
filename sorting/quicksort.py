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

data = [8, 3, 2, 7, 9, 4, 1]
# data = [3, 1, 2]

print("ORIGINAL", data)

def as_list(x):
    if type(x) is list:
        return x
    else:
        return [x]

def partition(arr):
    pivot = len(arr) - 1
    left = 0
    right = len(arr) - 2

    while left <= right:
        while left <= len(arr) - 2 and arr[left] < arr[pivot]:
            left += 1
        while right >= 0 and arr[right] >= arr[pivot]:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[left], arr[pivot] = arr[pivot], arr[left]

    front = as_list(arr[0:left])
    if len(front) > 1:
        front = partition(front)
    
    middle = as_list(arr[left])
    
    back = as_list(arr[(left+1):])
    if len(back) > 1:
        back = partition(back)
    
    print(front, middle, back)
    
    return front + middle + back


print("SOLVED  ", partition(data))




    

    
        




