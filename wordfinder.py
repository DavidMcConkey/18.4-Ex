"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """
    A class used to read a doc of the user's choosing and return a 
    random word from it

    """

    def __init__(self, link):
        """Reads dictionary and returns num of items read"""
        dict = open(link)

        self.words = self.parse(dict)

        print(f"{len(self.words)} words in file.")

    def parse(self, dict):
        """Parses dictionary for a list of the words"""
        return [w.strip() for w in dict]

    def random(self):
        """Returns random word from words list"""
        return random.choice(self.words)
