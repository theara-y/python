def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    openCount = 0
    for x in parens:
        if x == "(":
            openCount += 1
        elif x == ")":
            if openCount <= 0:
                return False
            else:
                openCount -= 1
    return openCount == 0