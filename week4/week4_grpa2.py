"""
Week 4 - GRPA 2: Master Water Tank

Problem:
--------
Given n water tanks on a hill connected by m directed pipes (water flows
one way), find a "master tank" — a tank from which connecting a single
water source can fill ALL other tanks.

Formally: find a vertex in a directed graph from which every other vertex
is reachable. Return 0 if no such vertex exists.

Approach (O(n + m)):
--------------------
1. Find all Strongly Connected Components (SCCs) via Kosaraju's algorithm.
2. Build the condensation DAG (each SCC becomes a super-node).
3. In a DAG, if there is EXACTLY ONE node with in-degree 0, it is the
   sole source and can reach every other node — the master SCC.
4. Return any tank from that SCC. If multiple or zero sources exist,
   return 0.

Why step 3 works:
  In a DAG with a single source S, every node v has a backward path of
  edges that must ultimately reach a node with in-degree 0. Since S is
  the only such node, all nodes are reachable from S.

Example (GT from problem):
  tanks = [1, 2, 3, 4]
  pipes = [(1,2), (2,3), (2,4)]
  → Tank 1 is the only master tank → return 1
"""

from collections import deque


# ---------------------------------------------------------------------------
# Core algorithm
# ---------------------------------------------------------------------------

def findMasterTank(tanks: list[int], pipes: list[tuple[int, int]]) -> int:
    """
    Find a master tank from which all tanks can be filled.

    Uses Kosaraju's SCC algorithm + condensation DAG analysis in O(n + m).

    Args:
        tanks: List of tank numbers (1-indexed, arbitrary ordering).
        pipes: List of directed edges (u, v) meaning water flows u → v.

    Returns:
        A master tank number, or 0 if none exists.
    """
    if not tanks:
        return 0

    # Build adjacency lists (original + reversed graph)
    adj  = {t: [] for t in tanks}   # original  : u → [v, ...]
    radj = {t: [] for t in tanks}   # reversed  : v → [u, ...]

    for u, v in pipes:
        if u in adj and v in adj:
            adj[u].append(v)
            radj[v].append(u)

    # ------------------------------------------------------------------
    # Kosaraju Step 1 — iterative DFS on original graph, record finish
    # ------------------------------------------------------------------
    visited: set[int] = set()
    finish_order: list[int] = []

    def dfs_original(start: int) -> None:
        """Iterative post-order DFS; appends to finish_order on exit."""
        stack = [(start, iter(adj[start]))]
        visited.add(start)
        while stack:
            node, children = stack[-1]
            try:
                child = next(children)
                if child not in visited:
                    visited.add(child)
                    stack.append((child, iter(adj[child])))
            except StopIteration:
                finish_order.append(node)
                stack.pop()

    for tank in tanks:
        if tank not in visited:
            dfs_original(tank)

    # ------------------------------------------------------------------
    # Kosaraju Step 2 — iterative DFS on reversed graph in reverse
    #                   finish order → each traversal is one SCC
    # ------------------------------------------------------------------
    visited2: set[int] = set()
    scc_of: dict[int, int] = {}   # tank → SCC id
    sccs: list[list[int]] = []    # SCC id → list of tanks

    def dfs_reversed(start: int, scc_id: int) -> None:
        """Iterative DFS on the reversed graph to collect one SCC."""
        stack = [start]
        visited2.add(start)
        scc_of[start] = scc_id
        sccs[scc_id].append(start)
        while stack:
            node = stack.pop()
            for parent in radj[node]:
                if parent not in visited2:
                    visited2.add(parent)
                    scc_of[parent] = scc_id
                    sccs[scc_id].append(parent)
                    stack.append(parent)

    for tank in reversed(finish_order):
        if tank not in visited2:
            new_id = len(sccs)
            sccs.append([])
            dfs_reversed(tank, new_id)

    num_sccs = len(sccs)

    # ------------------------------------------------------------------
    # Build condensation DAG and count in-degrees
    # ------------------------------------------------------------------
    in_degree = [0] * num_sccs
    seen_edges: set[tuple[int, int]] = set()

    for u, v in pipes:
        su, sv = scc_of.get(u, -1), scc_of.get(v, -1)
        if su == -1 or sv == -1 or su == sv:
            continue                      # same SCC → internal edge
        edge = (su, sv)
        if edge not in seen_edges:
            seen_edges.add(edge)
            in_degree[sv] += 1

    # ------------------------------------------------------------------
    # Find source SCCs (in-degree 0 in condensation DAG)
    # ------------------------------------------------------------------
    sources = [i for i in range(num_sccs) if in_degree[i] == 0]

    if len(sources) != 1:
        # Multiple or zero sources → no unique master tank
        return 0

    # Return the smallest-numbered tank in the master SCC (deterministic)
    return min(sccs[sources[0]])


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def _run_tests() -> None:
    sep = "-" * 52
    print(sep)
    print(f"{'Test':<28} {'Expected':>8}  {'Got':>6}  {'Pass?':>5}")
    print(sep)

    cases: list[tuple[str, list[int], list[tuple[int,int]], int]] = [
        (
            "Example GT (problem)",
            [1, 2, 3, 4],
            [(1, 2), (2, 3), (2, 4)],
            1,
        ),
        (
            "Linear chain 1→2→3→4",
            [1, 2, 3, 4],
            [(1, 2), (2, 3), (3, 4)],
            1,
        ),
        (
            "Two sources (no master)",
            [1, 2, 3],
            [(1, 3), (2, 3)],
            0,
        ),
        (
            "Disconnected (no master)",
            [1, 2, 3, 4],
            [(1, 2), (3, 4)],
            0,
        ),
        (
            "Single node",
            [1],
            [],
            1,
        ),
        (
            "Cycle: 1↔2, both reach 3",
            [1, 2, 3],
            [(1, 2), (2, 1), (1, 3)],
            # SCC {1,2} is the only source; min of {1,2} = 1
            1,
        ),
        (
            "Full cycle (all same SCC)",
            [1, 2, 3],
            [(1, 2), (2, 3), (3, 1)],
            # One SCC with in-degree 0 → master exists
            1,
        ),
        (
            "Star from node 5",
            [1, 2, 3, 4, 5],
            [(5, 1), (5, 2), (5, 3), (5, 4)],
            5,
        ),
    ]

    for name, tanks, pipes, expected in cases:
        result = findMasterTank(tanks, pipes)
        # For "any valid master" cases, verify reachability instead of exact match
        ok = _verify(tanks, pipes, result, expected)
        status = "✓" if ok else "✗"
        print(f"{name:<28} {expected:>8}  {result:>6}  {status:>5}")

    print(sep)


def _verify(
    tanks: list[int],
    pipes: list[tuple[int, int]],
    result: int,
    expected: int,
) -> bool:
    """
    Accept result if:
      - expected == 0 and result == 0, OR
      - expected != 0 and result != 0 and result can reach all tanks.
    """
    if expected == 0:
        return result == 0
    if result == 0:
        return False
    # BFS reachability check
    adj = {t: [] for t in tanks}
    for u, v in pipes:
        adj[u].append(v)
    reachable: set[int] = set()
    queue = deque([result])
    reachable.add(result)
    while queue:
        node = queue.popleft()
        for nbr in adj[node]:
            if nbr not in reachable:
                reachable.add(nbr)
                queue.append(nbr)
    return reachable == set(tanks)


if __name__ == "__main__":
    _run_tests()

