def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1)
    str2 = str(num2)
    if len(str1) != len(str2):
        return False

    set1 = set(str1)
    set2 = set(str2)
    if len(set1) != len(set2):
        return False

    for each in set1:
        if each not in set2:
            return False

    for target in set1:
        size1 = len([x for x in str1 if x == target])
        size2 = len([x for x in str2 if x == target])
        if size1 != size2:
            return False

    return True
