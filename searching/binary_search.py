"""
BINARY SEARCH
Time Complexity: O(N)
Auxilary Space: O(1)
"""

data = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
find = 120

print("FIND", find, "IN", data)

def binary_search_iterative(data, find):
    low = 0
    high = len(data) - 1

    while low != high:

        middle = int((high - low)/2 + low)

        if data[middle] == find:
            return middle
        
        elif find > data[middle]:
            low = middle + 1

        else:
            high = middle - 1

    if data[low] == find:
        return low
    
    return -1

def binary_search_recursive(data, find, low, high):
    
    middle = int((high - low)/2 + low)

    if data[middle] == find:
        return middle
    
    elif low == high:
        return low if data[low] == find else -1

    elif find > data[middle]:
        return binary_search_recursive(data, find, middle + 1, high)
    
    else:
        return binary_search_recursive(data, find, low, middle - 1)
 
print("BINARY SEARCH RECURSIVE", binary_search_recursive(data, find, 0, len(data) - 1))
print("BINARY SEARCH ITERATIVE", binary_search_iterative(data, find))
