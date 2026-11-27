"""
Write a function findRedundantEdges(E,n) that accept an edge list E in increasing order of the edge weight where all edge weights are distinct and the number of vertices n (labeled from 0 to n-1) in a connected undirected graph and the function returns a list of redundant edges in increasing order of weight, so by removing these edges, the graph should remain connected with the minimum total cost of edges(minimum cost spanning tree). Try to write solution code of complexity O((E+V)logV).


Note - Selected edges tuples in the output list should be similar to input list edges tuples.

Hint- Union-find data structure


Sample input 2

4
[(0,1,10),(1,2,20),(2,3,30),(3,0,40),(1,3,50)]
Output

[(3, 0, 40), (1, 3, 50)]
"""


def findRedundantEdges(
    E: list[tuple[int, int, int]], n: int
) -> list[tuple[int, int, int]]:
    """Return list of redundant edges not part of the Minimum Spanning Tree (MST)."""
    parent = list(range(n))
    rank = [0] * n

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True

    redundant: list[tuple[int, int, int]] = []
    for edge in E:
        u, v, _ = edge
        if not union(u, v):
            redundant.append(edge)

    return redundant


if __name__ == "__main__":
    sample_edges = [
        (0, 1, 10),
        (1, 2, 20),
        (2, 3, 30),
        (3, 0, 40),
        (1, 3, 50),
    ]
    expected = [(3, 0, 40), (1, 3, 50)]
    assert findRedundantEdges(sample_edges, 4) == expected

    # Tree with no redundant edges
    tree_edges = [(0, 1, 5), (1, 2, 10)]
    assert findRedundantEdges(tree_edges, 3) == []

    print("All checks passed.")
