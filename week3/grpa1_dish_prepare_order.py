"""GRPA 1 — Dish preparation order (frequency sort with tie-breaking by ID)."""


def dish_prepare_order(order_list: list[int]) -> list[int]:
    """Return dish IDs sorted by order frequency descending, then by ID ascending.

    Counts how many times each dish ID appears in `order_list`, then returns
    the unique IDs sorted so that the most-ordered dish comes first.
    Ties in frequency are broken by ascending dish ID.

    Args:
        order_list: List of dish IDs representing each individual order received.

    Returns:
        Unique dish IDs in the order the restaurant will prepare them.

    Time:  O(n + k log k)  where n = len(order_list), k = unique dish count
    Space: O(k)            for the frequency map
    """
    frequency: dict[int, int] = {}
    for dish_id in order_list:
        frequency[dish_id] = frequency.get(dish_id, 0) + 1

    sorted_dishes = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    return [dish_id for dish_id, _ in sorted_dishes]


# ---------------------------------------------------------------------------
# Backward-compatible alias matching the original graded assignment signature
# ---------------------------------------------------------------------------
DishPrepareOrder = dish_prepare_order
