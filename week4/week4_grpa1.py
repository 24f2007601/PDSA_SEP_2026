"""
Week 4 - Problem 1: Social Network Connectivity Level

Problem:
--------
Consider a social network of friends/relatives visualized as a graph where:
  - Each vertex denotes a person.
  - An edge between two vertices means those two people know each other.
  - Level of connectivity = minimum number of hops between two persons.
      * Direct connection → level 1
      * Friend-of-a-friend (no direct link) → level 2
      * And so on...
  - Connectivity is undirected (bidirectional).

Task:
-----
Complete findConnectionLevel(n, Gmat, Px, Py) that returns the minimum level
of connectivity between persons Px and Py.
Return 0 if Px and Py are not connected at all.

Example graph (7 persons, 0–6):

        0
       / \
      1---2
     /|\ /|
    / | X | \
   /  |/ \|  \
  3---4   5---6
       \ /
        (4-5)

Edges: 0-1, 0-2, 1-2, 1-3, 1-4, 1-5, 2-3, 2-5, 3-4, 4-5, 5-6
"""

from collections import deque


def findConnectionLevel(n: int, Gmat: list[list[int]], Px: int, Py: int) -> int:
    """
    Find the minimum level of connectivity between persons Px and Py
    using Breadth-First Search (BFS).

    BFS guarantees the shortest path in an unweighted graph, which
    corresponds directly to the minimum connectivity level.

    Args:
        n:     Number of persons (nodes numbered 0 to n-1).
        Gmat:  n×n adjacency matrix; Gmat[x][y] == 1 means x and y are
               directly connected.
        Px:    Source person index.
        Py:    Target person index.

    Returns:
        Minimum connectivity level (shortest path length) between Px and Py.
        Returns 0 if they are the same person OR if no path exists.
    """
    if Px == Py:
        return 0

    # BFS: each queue entry is (current_node, current_level)
    visited = [False] * n
    visited[Px] = True
    queue = deque([(Px, 0)])

    while queue:
        current, level = queue.popleft()

        for neighbor in range(n):
            if Gmat[current][neighbor] == 1 and not visited[neighbor]:
                next_level = level + 1
                if neighbor == Py:
                    return next_level
                visited[neighbor] = True
                queue.append((neighbor, next_level))

    # Py was never reached → no connection
    return 0


# ---------------------------------------------------------------------------
# Example / Test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # 7-person graph from the problem illustration
    # Edges: 0-1, 0-2, 1-2, 1-3, 1-4, 1-5, 2-3, 2-5, 3-4, 4-5, 5-6
    n = 7
    Gmat = [
        [0, 1, 1, 0, 0, 0, 0],  # 0: knows 1, 2
        [1, 0, 1, 1, 1, 1, 0],  # 1: knows 0, 2, 3, 4, 5
        [1, 1, 0, 1, 0, 1, 0],  # 2: knows 0, 1, 3, 5
        [0, 1, 1, 0, 1, 0, 0],  # 3: knows 1, 2, 4
        [0, 1, 0, 1, 0, 1, 0],  # 4: knows 1, 3, 5
        [0, 1, 1, 0, 1, 0, 1],  # 5: knows 1, 2, 4, 6
        [0, 0, 0, 0, 0, 1, 0],  # 6: knows 5
    ]

    test_cases = [
        (0, 6, 3),  # 0→1→5→6              (level 3)
        (0, 5, 2),  # 0→1→5 or 0→2→5       (level 2)
        (0, 1, 1),  # direct edge           (level 1)
        (0, 0, 0),  # same person           (level 0)
        (3, 6, 3),  # 3→4→5→6 or 3→1→5→6   (level 3)
        (6, 0, 3),  # reverse: 6→5→1→0      (level 3)
    ]

    print(f"{'Px':>4}  {'Py':>4}  {'Expected':>10}  {'Got':>6}  {'Pass?':>6}")
    print("-" * 44)
    for Px, Py, expected in test_cases:
        result = findConnectionLevel(n, Gmat, Px, Py)
        status = "✓" if result == expected else "✗"
        print(f"{Px:>4}  {Py:>4}  {expected:>10}  {result:>6}  {status:>6}")

