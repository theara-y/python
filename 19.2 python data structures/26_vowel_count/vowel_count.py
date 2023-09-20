def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    filtered = [ x for x in phrase.lower() if x in "aeiou" ]
    result = dict()
    for x in filtered:
        if result.get(x) == None:
            result[x] = 1
        else:
            result[x] += 1
    return result