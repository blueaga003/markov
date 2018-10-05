"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text_source = open(file_path)
    file_as_string = text_source.read()
    return file_as_string   

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    bigrams_with_following_text = {}
 
    words = text_string.split()
    bigram_values = []
    word_index = 0

   
    # minus two because index out of range for later use
    for word_index in range(len(words) - 2):
        word_pairs = tuple((words[word_index], words[word_index + 1]))
        
        value = bigrams_with_following_text.get(word_pairs, [])
        value.append(words[word_index + 2])
        bigrams_with_following_text[word_pairs] = value 
    
    return bigrams_with_following_text


def make_text(chains):
    """Return text from chains."""

    words = []
    #unigrams_with_following_text = {}

    # your code goes here
    #for each tuple combination, we want to pull the second word in the tuple and append it to the list
    # then we chose a random word from the inital tuple combination and append it to the new list
    # from there we look up the new tuple combination in the dictionary (combination of second word in first tuple
    # and random word from list) and repeat.


    for word in chains:
        words.append(word[1])
        choice(chains[word])
        word_pairs = (word[1], choice(chains[word]))
        if word_pairs in chains.keys():
            chains[word_pairs]
        else:
            return " ".join(words)

if len(sys.argv) != 2:
	print("<USAGE ERROR> python3 markov.py text_input")
	sys.exit()
else:
	input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains_in_dictionary_format = make_chains(input_text)
make_text(chains_in_dictionary_format)
# Produce random text
random_text = make_text(chains_in_dictionary_format)
print(random_text)
#print(random_text)
