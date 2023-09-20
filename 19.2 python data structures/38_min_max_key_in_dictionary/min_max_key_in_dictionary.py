def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    k = list(d.keys())
    highest = k[0]
    lowest = k[0]

    for i in range(1, len(k)):
        if k[i] > highest:
            highest = k[i]
        if k[i] < lowest:
            lowest = k[i]

    return(lowest, highest)