"""
You have a deck of shuffled cards ranging from 0 to 100,000,000.
There are 2 subordinates below you and two subordinates below them and so on.

- Each subordinate splits their deck into two halves and gives each half to their two subordinates.
- If a subordinate receives only two cards, they sort and return them.
- If a subordinate receives only one card, they return it as-is.
- When subordinates return sorted halves, the superior merges them in ascending order.

Write the function def subordinates(L) that returns a tuple:
    (sorted_list, number_of_people_involved)

Sample Input 1: [194, 69, 103, 150, 151, 44, 103, 98]
Output:         ([44, 69, 98, 103, 103, 150, 151, 194], 7)

Sample Input 2: [10, 33, 45, 67, 92, 100, 5]
Output:         ([5, 10, 33, 45, 67, 92, 100], 7)
"""


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def subordinates(L):
    n = len(L)
    if n <= 1:
        return (L, 1)
    if n == 2:
        return (sorted(L), 1)

    mid = n // 2
    left_sorted, left_count = subordinates(L[:mid])
    right_sorted, right_count = subordinates(L[mid:])

    return (_merge(left_sorted, right_sorted), 1 + left_count + right_count)


L = list(map(int, input().strip().strip("[]").split(",")))
print(subordinates(L))
