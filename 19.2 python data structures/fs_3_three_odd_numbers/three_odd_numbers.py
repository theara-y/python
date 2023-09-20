def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    stringRep = ""
    for num in nums:
        if num % 2 == 0:
            stringRep += "even"
        else:
            stringRep += "odd"

    if "oddoddodd" in stringRep:
        return True
    if "evenevenodd" in stringRep:
        return True
    if "evenoddeven" in stringRep:
        return True
    if "oddeveneven" in stringRep:
        return True
    return False