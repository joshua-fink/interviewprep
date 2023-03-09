"""
SELECTION SORT

Strengths: Intuitive, space efficent
Weaknesses: SLOW on big data sets

Complexity
    Worst case time: O(n^2)
    Best case time: O(n^2)
    Avg case time: O(n^2)
    Space: O(1)
"""

data = [8, 3, 2, 7, 4, 9, 1, 4]

print("ORIGINAL", data)

for i in range(0, len(data)):
    small_index = i
    for j in range(i, len(data)):
        if data[small_index] > data[j]:
            small_index = j
    
    data[i], data[small_index] = data[small_index], data[i]

print("SOLVED  ", data)
