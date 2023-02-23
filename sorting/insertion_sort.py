"""
INSERTION SORT

Strengths: Intuitive, space efficent, fast on sorted list
Weaknesses: SLOW on big data sets

Complexity
    Worst case time: O(n^2)
    Best case time: O(n)
    Avg case time: O(n^2)
    Space: O(1)
"""

data = [8, 3, 2, 7, 9, 4, 1]

print("ORIGINAL", data)

for i in range(0, len(data)):
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else: 
            break

print("SOLVED  ", data)
        