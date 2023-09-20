from random import random
import math
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
        >>> special_word_finder = SpecialWordFinder()
        >>> special_word_finder.words = ["#fruits"]
        >>> print(special_word_finder.random())
        None
        >>> special_word_finder.words = ["#fruits", "apple"]
        >>> print(special_word_finder.random())
        apple
    """
    def __init__(self, filename = None):
        super().__init__(filename)

    def random(self):
        """ Randomly returns a non-commented line """
        nonComments = [ word for word in self.words if word[0] != "#" ]
        if len(nonComments) == 0:
            return None
        return nonComments[math.floor(random() * len(nonComments))]
