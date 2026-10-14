#question 
"""
Problem Statement

Complete the python function findLargest(L) below, which accepts a list L of unique numbers, that are sorted(ascending) and rotated n times, where n is unknown, and returns the largest number in list L. Rotating list [2, 4, 5, 7, 8] one time gives us list [8, 2, 4, 5, 7], and rotating the second time gives list [7, 8, 2, 4, 5] and so on. Try to give an 
O
(
l
o
g
 
n
)
O(log n)solution. Hint: One of the 
O
(
l
o
g
 
n
)
O(log n) solutions can be implemented using binary search and using 'first or last' element to know, the direction of searching further.

# input<L>: List L sorted and rotated.
# out: Return the largest number in list L.
def findLargest(L):
    # Your code goes here
Sample input:

7, 8, 2, 4, 5
Sample output:

8
 

Note:- Do not use list slicing in the binary search implementation because the list slicing operation is of order O(n).
"""
def findLargest(L):
    low = 0
    high = len(L) - 1
    

    if L[low] <= L[high]:
        return L[high]
        
    while low <= high:
        mid = (low + high) // 2
        

        if mid < len(L) - 1 and L[mid] > L[mid + 1]:
            return L[mid]
        if mid > 0 and L[mid] < L[mid - 1]:
            return L[mid - 1]
            

        if L[mid] >= L[low]:

            low = mid + 1
        else:

            high = mid - 1
            
    return L[low]
