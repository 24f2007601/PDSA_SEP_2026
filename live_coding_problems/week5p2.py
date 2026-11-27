"""
You are given a network of n nodes, labelled from 0 to n-1. You are also given travel_times, a list of signal travel times in as directed edges travel_times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

Write a function min_transmission_time(n, travel_times, s) that accept number of nodes n, a list travel_times and a source node s to send the signal . The function returns the minimum time required for the signal sent by the source node s to be received by all the remaining n-1 nodes. If it is impossible to obtain a signal for all n-1 nodes, return -1.

Sample Input 1

4 #n
[(1,0,1),(1,2,1),(2,3,1)] #travel_times
2 #s
Output

2
"""

import heapq


def min_transmission_time(
    n: int, travel_times: list[tuple[int, int, int]], s: int
) -> int:
    """Return minimum time for signal from source s to reach all n nodes, or -1."""
    adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in travel_times:
        adj[u].append((v, w))

    dist: dict[int, int] = {}
    heap: list[tuple[int, int]] = [(0, s)]

    while heap:
        time, u = heapq.heappop(heap)
        if u in dist:
            continue
        dist[u] = time
        for v, w in adj[u]:
            if v not in dist:
                heapq.heappush(heap, (time + w, v))

    return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    # Sample input test
    assert min_transmission_time(4, [(1, 0, 1), (1, 2, 1), (2, 3, 1)], 1) == 2

    # Unreachable test
    assert min_transmission_time(4, [(1, 0, 1), (1, 2, 1), (2, 3, 1)], 2) == -1

    # Single node test
    assert min_transmission_time(1, [], 0) == 0

    print("All checks passed.")
