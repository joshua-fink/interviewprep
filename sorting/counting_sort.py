"""
COUNTING SORT

Strengths: Linear time
Weaknesses: Restricted inputs, space cost

Complexity
    Worst case time: O(n)
    Best case time: O(n)
    Avg case time: O(n)
    Space: O(n)
"""

data = [8, 3, 2, 7, 4, 9, 1, 4]

print("ORIGINAL", data)

counts = [0] * 10

for elt in data:
    counts[elt] += 1

solution = []

for index in range(0,10,1):
    for i in range(0,counts[index]):
        solution.append(index)

print("SOLVED  ", solution)