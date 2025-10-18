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


    def generate(self, seed_term=None, term_count = 15):
        '''
        Generate sentences using the Markov property.

        Parameters:
        seed_term (str): An optional term from the corpus
        term_count (int): The number of terms you want generated

        Return value:
        ' '.join(result) (str): A sentence constructed using terms
        and spaces inserted in between them.
        '''
        if self.term_dict is None:
            self.get_term_dict()
        
        # Choose a random seed_term from the dictionary
        # keys if one is not provided in the input.
        if seed_term is None:
            seed_term = np.random.choice(list(self.term_dict.keys()))
        elif seed_term not in self.term_dict:
            raise ValueError(f"Seed term '{seed_term}' not found in corpus")
    
    # Initialize the results.
        result = [seed_term]
        current_term = seed_term

    # Produce the rest of the terms.
        for i in range(term_count - 1):

            # If the current term doesn't have words after it or isn't
            # in the dictionary, then choose a random term from the
            # dictionary keys.
            if current_term not in self.term_dict or not self.term_dict[current_term]:
                current_term = np.random.choice(list(self.term_dict.keys()))
            else:
                # Choose the next term randomly from the list of
                # potential next terms.
                current_term = np.random.choice(self.term_dict[current_term])
            result.append(current_term)

            # Return the terms with spaces in between them.
        return ' '.join(result)
