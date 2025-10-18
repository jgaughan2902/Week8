from collections import defaultdict
import numpy as np


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None
        self.get_term_dict()

    def get_term_dict(self):
        '''
        Build a term dictionary of Markov states

        Parameters:
        corpus (str): A corpus of text

        Return value:
        self.term_dict (dict): A dictionary of
        tokens (words)
        '''
        # Use defaultdict() to make an empty
        # list for new keys.
        term_dict = defaultdict(list)

        # Split the corpus into individual tokens (words)
        tokens = self.corpus.split()

        # For all words in the tokens object, you 
        # append next_token to the dictionary.
        for i in range(len(tokens) - 1):
            current_token = tokens[i]
            next_token = tokens[i + 1]
            term_dict[current_token].append(next_token)
        
        # Convert the defaultdict to a regular dictionary.
        self.term_dict = dict(term_dict)

        return self.term_dict


    def generate(self):