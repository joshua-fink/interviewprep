"""
LINEAR SEARCH
Time Complexity: O(N)
Auxilary Space: O(1)
"""

data = [10, 50, 30, 70, 80, 60, 20, 90, 40]
find = 20

print("FIND", find, "IN", data)

for index in range(0, len(data), 1):
    if data[index] == 20:
        print("FOUND", find, "at index", index)

print("NOT FOUND")