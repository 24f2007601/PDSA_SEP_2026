"""
Find best flight fare with at most k stops.

Given a weighted directed adjacency list flight_route, source, destination, and k (max intermediate stops),
returns (minimum_cost, [source, ..., destination]), or string 'Not found' if no such route exists.
"""

from collections import deque
from typing import Union


def best_fare(
    flight_route: dict[int, list[tuple[int, int]]],
    source: int,
    destination: int,
    k: int,
) -> Union[tuple[int, list[int]], str]:
    """Return (min_cost, path) with at most k intermediate stops, or 'Not found'."""
    best_cost: float = float("inf")
    best_path: list[int] = []

    # queue holds (current_node, current_cost, path, stops_count)
    # stops_count counts intermediate stops visited so far
    queue: deque[tuple[int, int, list[int], int]] = deque([(source, 0, [source], 0)])

    # min_stops_for_state[(node, cost)] is not needed;
    # track min_cost for (node, stops)
    min_cost_at: dict[tuple[int, int], int] = {}

    while queue:
        curr, cost, path, stops = queue.popleft()

        if curr == destination:
            if cost < best_cost:
                best_cost = cost
                best_path = path
            continue

        # If we already have k intermediate stops, we can only fly directly to destination
        if stops > k:
            continue

        for neighbor, price in flight_route.get(curr, []):
            next_cost = cost + price
            next_stops = stops + 1 if neighbor != destination else stops

            if next_stops <= k or neighbor == destination:
                state = (neighbor, next_stops)
                if next_cost < min_cost_at.get(state, float("inf")):
                    min_cost_at[state] = next_cost
                    if next_cost < best_cost:
                        queue.append((neighbor, next_cost, path + [neighbor], next_stops))

    if best_cost == float("inf"):
        return "Not found"

    return (int(best_cost), best_path)


if __name__ == "__main__":
    edges = [
        (0, 1, 1000), (0, 2, 500), (0, 3, 3000), (2, 0, 2000),
        (2, 1, 3000), (1, 3, 300), (3, 4, 600), (2, 4, 2000),
    ]
    graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(5)}
    for u, v, w in edges:
        graph[u].append((v, w))

    # Sample 1: k=1 -> (2500, [0, 2, 4])
    assert best_fare(graph, 0, 4, 1) == (2500, [0, 2, 4])

    # Sample 2: k=0 -> Not found
    assert best_fare(graph, 0, 4, 0) == "Not found"

    # Direct edge test if exists: 0 -> 1 with k=0
    assert best_fare(graph, 0, 1, 0) == (1000, [0, 1])

    # k=2: 0 -> 1 -> 3 -> 4 (stops=2, cost=1000+300+600=1900)
    assert best_fare(graph, 0, 4, 2) == (1900, [0, 1, 3, 4])

    print("All checks passed.")
