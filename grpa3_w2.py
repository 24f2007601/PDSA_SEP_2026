#question 3 
"""
Merging two sorted arrays in place.

Given a custom implementation of list named MyList. On MyList objects you can perform read operations similar to the in-build lists in Python, example use A[i] to read element at index i in MyListobject A. The only possible operation that you can use to edit data in MyList objects is by calling the swap method. For instance, A.swap(indexA, B, indexB) will swap values at A[indexA] and B[indexB]and A.swap(index1, A, index2) will swap values at A[index1] and A[index2], where indexA, indexB, index1, index2 are all integers.

Complete the Python function mergeInPlace(A, B) that accepts two MyLists A and B containing integers that are sorted in ascending order and merges them in place(without using any other list) such that after merging, A and B are still sorted in ascending order with the smallest element of both MyLists as the first element of A.

# Complete this function
def mergeInPlace(A, B):
  # Your code goes here
Note:- Your function should not return any list and should only merge the given sorted lists inplace.

 

Sample Input:

2 4 6 9 13 15
1 3 5 10
Sample Output:

1 2 3 4 5 6
9 10 13 15
Sample Input:

4 6 
1 3 6 10
Sample Output:

1 3
4 6 6 10
"""
def mergeInPlace(A, B):
    n = len(A)
    m = len(B)
    
    
    if n == 0 or m == 0:
        return
        
   
    for i in range(n):
        
        if A[i] > B[0]:
            
            A.swap(i, B, 0)
            
            
            j = 0
            while j < m - 1 and B[j] > B[j + 1]:
                B.swap(j, B, j + 1)
                j += 1
