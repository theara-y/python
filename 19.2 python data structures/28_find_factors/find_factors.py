def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    result = []
    for i in range(1, num//2):
        if i not in result:
            if num % i == 0:
                quotient = int(num / i)
                result.append(i)
                result.append(quotient)

    result.sort()
    return result
