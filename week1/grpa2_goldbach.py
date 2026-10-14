"""GRPA 2 — Goldbach's Conjecture (prime-pair decomposition)."""


def is_prime(num: int) -> bool:
    """Return True if `num` is a prime number."""
    if num <= 1:
        return False
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            return False
    return True


def goldbach(n: int) -> list[tuple[int, int]]:
    """Return all prime pairs (a, b) where a <= b and a + b == n.

    Iterates `a` from 2 to n//2 and checks primality of both `a` and `n - a`.

    Time:  O(n √n)
    """
    pairs: list[tuple[int, int]] = []

    for a in range(2, (n // 2) + 1):
        b = n - a
        if is_prime(a) and is_prime(b):
            pairs.append((a, b))

    return pairs
