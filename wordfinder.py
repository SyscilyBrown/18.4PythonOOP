"""Word Finder: finds random words from a dictionary."""
""" import words"""

import random 

class WordFinder:
    """find random words from dictionary
    >>> word_finder = WordFinder("simple.text")
    3 words read
    >>>wf.random() in ["cat", "dog", "porcupine"]
    True

    >>>wf.random() in ["cat", "dog", "porcupine"]
    True

    >>>wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """df = dictionary file. read dictionary and reports number of items read"""
        df = open(path)

        self.words = self.parse(df)

        print(f"{len(self.words)} words read")

    def parse(self, df):
     """parse df into list of words"""
     return [w.strip() for w in df]

    def random(self):
        """return random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Excludes blank lines/comments"""
    def parse(self, df):
        """parse df into list of words, skipping blamnks/comments."""

        return [w.strip() for w in df
        if w.strip() and not w.startswith("#")]
