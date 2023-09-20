def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    filtered = {x for x in nums if x <= goal}
    numbers_found = []
    pairs = []
    
    for firstNum in filtered:
        if firstNum not in pairs:
            otherNum = goal - firstNum
            if otherNum != firstNum and otherNum in nums:
                numbers_found.extend([firstNum, otherNum])
                pairs.append([firstNum, otherNum])

            elif otherNum == firstNum:
                if len([x for x in nums if x == firstNum]) > 1:
                    numbers_found.append(firstNum)
                    pairs.append([firstNum, firstNum])

    bestIndex = len(nums)
    bestPair = ()

    for pair in pairs:
        first = pair[0]
        second = pair[1]
        firstIndex = None
        secondIndex = None
        if first != second:
            firstIndex = nums.index(first)
            secondIndex = nums.index(second)
        else:
            firstIndex = nums.index(first)
            secondIndex = nums[firstIndex + 1:].index(second) + firstIndex + 1

        greaterIndex = max(firstIndex, secondIndex)
        lesserIndex = min(firstIndex, secondIndex)
        if greaterIndex < bestIndex:
            bestIndex = greaterIndex
            bestPair = (nums[lesserIndex], nums[greaterIndex])

    return bestPair

    