import math

"""
HEAPSORT

Strengths: Fast, space efficient
Weaknesses: Slow in practice -> asymptotic complexity ignores constants

Complexity
    Worst case time: O(n lg n)
    Best case time: O(n)
    Avg case time: O(n lg n)
    Space: O(1)
"""

data = [8, 1, 2, 7, 9, 3, 4, 5]
print("ORIGINAL", data)

def get_left_child(index):
    return index * 2 + 1

def get_right_child(index):
    return index * 2 + 2

def get_level_index(height):
    return 2**height - 1

def heapify(arr):
    height = math.ceil(math.log2(len(arr) - 1 + 2)) - 1

    for level in range(height - 1, -1, -1):
        first_index = get_level_index(level)
        second_index = get_level_index(level + 1) - 1

        if (len(arr) - 1 > second_index):
            second_index = len(arr) - 1

        for parent in range(first_index, second_index + 1, 1):

            left_child = get_left_child(parent)
            right_child = get_right_child(parent)

            if left_child > (len(arr) - 1):
                break

            if right_child > (len(arr) - 1):
                right_child = left_child

            if not (arr[left_child] < arr[parent] and arr[right_child] < arr[parent]):
                max_child = left_child

                if (arr[left_child] < arr[right_child]):
                    max_child = right_child

                arr[parent], arr[max_child] = arr[max_child], arr[parent]

    return arr

def heapsort(arr):

    for index in range(len(arr) - 1, -1, -1):
        
        arr[0], arr[index] = arr[index], arr[0]
        end = index - 1

        parent = 0
        left_child = get_left_child(parent)
        
        if left_child <= end:
            
            right_child = get_right_child(parent)
            if right_child > end: right_child = left_child

            while not ((arr[parent] > arr[left_child]) and (arr[parent] > arr[right_child])):
                    
                max_child = left_child

                if (arr[left_child] < arr[right_child]):
                    max_child = right_child

                arr[parent], arr[max_child] = arr[max_child], arr[parent]

                parent = max_child

                left_child = get_left_child(parent)
                if left_child > end: break

                right_child = get_right_child(parent)
                if right_child > end: right_child = left_child

    return arr

def heapsort_wrapper(arr):
    arr = heapify(arr)
    arr = heapsort(arr)
    return arr

print("SOLVED  ", heapsort_wrapper(data))




    
