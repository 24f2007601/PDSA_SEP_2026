"""
The government decides to construct a new railway station. Railway authorities provide a list of scheduled trains in a day with arrival time and departure time. Find the minimum number of platforms required for the railway station so that no train is kept waiting.

Write a function minimum_platform(train_schedule) that accepts a list of tuples train_schedule, where each tuple stores three values in the format (train_no(int),Arrival_time('HH:MM'),departure_time('HH:MM')).

The function should return the minimum number of platforms required for the railway station so that no train is kept waiting.

Sample Input

[(1,'09:00','09:10'),(2,'09:40','12:00'),(3,'09:50','11:20'),(4,'11:00','11:30'),(5,'11:40','12:10'),(6,'12:05','19:00'),(7,'12:06','13:00'),(8,'13:05','14:00'),(9,'14:05','15:00'),(10,'18:00','20:00')]
Output

3
"""


def minimum_platform(train_schedule: list[tuple[int, str, str]]) -> int:
    """Return the minimum number of platforms needed so no train waits."""
    arrivals = sorted(t[1] for t in train_schedule)
    departures = sorted(t[2] for t in train_schedule)

    platforms = max_platforms = 0
    i = j = 0
    n = len(train_schedule)

    while i < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms


if __name__ == "__main__":
    sample = [
        (1, '09:00', '09:10'), (2, '09:40', '12:00'), (3, '09:50', '11:20'),
        (4, '11:00', '11:30'), (5, '11:40', '12:10'), (6, '12:05', '19:00'),
        (7, '12:06', '13:00'), (8, '13:05', '14:00'), (9, '14:05', '15:00'),
        (10, '18:00', '20:00'),
    ]
    assert minimum_platform(sample) == 3
    assert minimum_platform([]) == 0
    print("All checks passed.")
