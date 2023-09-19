def print_upper_words(words, must_start_with = {}):
    """ 
    Given an array of words, prints each word in CAPS on per line

    Providing a set of lower case characters as the second argument will
    print only words beginning with a character in the set.
    If must_start_with is not provided, will print all words.


    >>> print_upper_words(["hello", "goodbye"])
    HELLO
    GOODBYE

    >>> print_upper_words(["hello", "goodbye"], {"h"})
    HELLO

    >>> print_upper_words(["hello", "goodbye"], {"h", "g"})
    HELLO
    GOODBYE
    
    """
    for word in words:
        if len(must_start_with) == 0 or word[0].lower() in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {})

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"e"})

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {"h", "g"})