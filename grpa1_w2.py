#question
"""
Problem Statement

Write a Python function combinationSort(strList) that takes a list of unique strings strList as an argument, where each string is a combination of a letter from a to z and a number from 0 to 99, the initial character in string being the letter. For example a23, d5, q99 are some strings in this format. This function should sorts the list and return two lists (L1, L2) in the order mentioned below.

L1: First list should contain all strings sorted in ascending order with respect to the first character only. All strings with same initial character should be in the same order as in the original list.

L2: In the list L1 above, sort the strings starting with same character, in descending order with respect to the number formed by the remaining characters.

Example:

Sample input 1:

d34, g54, d12, b87, g1, c65, g40, g5, d77
Sample output 1:

L1: b87, c65, d34, d12, d77, g54, g1, g40, g5
L2: b87, c65, d77, d34, d12, g54, g40, g5 ,g1
"""
def combinationSort(strList):
    
    L1 = sorted(strList, key=lambda x: x[0])
    
    
    L2 = sorted(strList, key=lambda x: (x[0], -int(x[1:])))
    
    return L1, L2


sample_input = ['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']
L1, L2 = combinationSort(sample_input)

print("L1:", ", ".join(L1))
print("L2:", ", ".join(L2))