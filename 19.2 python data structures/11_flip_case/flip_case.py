def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newString = ""
    for x in phrase:
        if x.lower() == to_swap.lower():
            if x.isupper():
                newString += x.lower()
            else:
                newString += x.upper()
        else:
            newString += x
    return newString
        