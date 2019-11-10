# Search the spambase.names file and use regular expressions to find the 
# words that correspond to the columns in spambase.data. More regex 
# details at https://en.wikipedia.org/wiki/Regular_expression

import re
import os

FILE_PATH = os.path.join('.', 'data', 'spambase.names')

def load_file():
    """
    Load the spambase.names file and write it to a long continious string.
    """
    s = ''

    with open(FILE_PATH) as f:
        for line in f:
            # .rstrip method gets rid of new line "\n" characters
            s = s + line.rstrip() 
    return s

def get_words():
    """ 
    Given a file path, find the words in the spambase using regular 
    expressions (regex). 
    """
    string = load_file()
    # Regex can be read as "Match any set of a-z characters word(s)
    #  after word_freq_ and before :"
    regex = re.compile(r'word_freq_([a-z]*):')
    # Use the regular expression to find all words.
    words = regex.findall(string)
    return words