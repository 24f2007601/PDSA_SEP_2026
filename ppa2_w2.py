#question
"""
Problem Statement

Consider a list L containing n integers, where each integer i is in the range [0, r) that is 0 <= i < r, r<1000 and n>>r (n is much greater than r).

Write a Python function sortInRange(L, r) to sort the list L in ascending order. Try to write a solution that runs in O(n + r) asymptotic complexity.

Sample Input:

L: 2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2
r: 4
Sample Output:

0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3
Note: In function, no need to return any list, just sort input list L in place.
"""
def sortInRange(L, r):
    # Step 1: Count occurrences of each number
    counts = [0] * r
    for num in L:
        counts[num] += 1
        
    # Step 2: Overwrite L in place with O(1) extra space per element
    index = 0
    for val in range(r):
        for _ in range(counts[val]):
            L[index] = val
            index += 1
