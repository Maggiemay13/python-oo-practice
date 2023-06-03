"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary words.txt

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()
    'eosin'

    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("words.txt")
        235886 words read


    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]
