def any7(nums):
    """
    Are any of these numbers a 7? (True/False)

    Run tests: python3 -m doctest -v file.py
    >>> any7([1, 2, 7, 4, 5])
    True

    >>> any7([1, 2, 4, 5])
    False
    """
    return 7 in nums

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

