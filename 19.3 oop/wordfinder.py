from random import random
import math

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, filename = None):
        self.words = []

        if filename != None:
            DIR = f"/home/tya/github/python/19.3 oop/{filename}"
            with open(DIR, "r") as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                    self.words.append(line.strip())
            
            print(f"{len(self.words)} words read")

    def random(self):
        return self.words[math.floor(random() * len(self.words))]