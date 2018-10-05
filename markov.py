"""Generate Markov text from text files."""

from random import choice
import sys
import pdb

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
    grams_with_following_text = {}
 
    words = text_string.split()
    gram_values = []
    word_index = 0
   
    # minus two because index out of range for later use
    for word_index in range(len(words) - ngram_value):
        #pdb.set_trace()
        word_combinations = tuple((words[word_index:word_index + ngram_value]))
        
        value = grams_with_following_text.get(word_combinations, [])
        value.append(words[word_index + (ngram_value)])
        grams_with_following_text[word_combinations] = value 
    
    return grams_with_following_text


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
       # print("this is word: {}".format(word))
        words.extend(word[1:])
       # print("this is the words list: {}".format(words))
        choice(chains[word])
        # pdb.set_trace()
        word_combinations = ()
        for entry in words[-ngram_value+1:]:
            word_combinations += tuple([entry])
            # print("the entry is: {}".format(entry))
        word_combinations += tuple([choice(chains[word])])

        # word_combinations = (word[1:] + tuple(choice(chains[word])))
        # print("this is word combinations {}".format(word_combinations))
        if word_combinations in chains.keys():
            chains[word_combinations]
        else:
            return " ".join(words)

if len(sys.argv) != 3:
    print("<USAGE ERROR> python3 markov.py text_input number_of_ngrams")
    sys.exit()
else:
    input_path = sys.argv[1]
    ngram_value = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains_in_dictionary_format = make_chains(input_text)
print(chains_in_dictionary_format)
make_text(chains_in_dictionary_format)
# Produce random text
random_text = make_text(chains_in_dictionary_format)
print(random_text)
#print(random_text)
