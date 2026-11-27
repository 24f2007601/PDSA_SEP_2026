import heapq


def Airport(distance_map: dict[int, list[tuple[int, int]]]) -> int:
    """Return the minimum total distance (MST) to connect all cities."""
    if not distance_map:
        return 0

    start = next(iter(distance_map))
    visited: set[int] = set()
    heap: list[tuple[int, int]] = [(0, start)]
    total = 0

    while heap and len(visited) < len(distance_map):
        dist, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        total += dist
        for v, w in distance_map[u]:
            if v not in visited:
                heapq.heappush(heap, (w, v))

    return total


if __name__ == "__main__":
    edges = [
        (0, 1, 10), (0, 2, 50), (0, 3, 300), (5, 6, 45), (2, 1, 30),
        (6, 4, 37), (1, 6, 65), (2, 5, 76), (1, 3, 40), (3, 4, 60), (2, 4, 20),
    ]
    distance_map: dict[int, list[tuple[int, int]]] = {i: [] for i in range(7)}
    for u, v, w in edges:
        distance_map[u].append((v, w))
        distance_map[v].append((u, w))

    assert Airport(distance_map) == 182
    assert Airport({}) == 0
    print("All checks passed.")
