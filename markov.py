"""Generate Markov text from text files."""

from random import choice
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
    bigrams_with_following_text = {}
    words = text_string.split()
    bigram_values = []
    word_index = 0

    print(words)
    for word_index in range(len(words) - 1):
        while word_index < len(words) - 2:
            # pdb.set_trace()
            #bigram_values.append(words[word_index + 2])
            diction_keys = (words[word_index], words[word_index + 1])
            bigrams_with_following_text[diction_keys] += [words[word_index + 2]]
            # bigrams_with_following_text[(words[word_index], words[word_index + 1])] += [words[word_index + 2]]
            

            #if word1 and word2 == key, append word3 to key list
            word_index += 1
    print(bigrams_with_following_text)

    # for key, value in bigrams_with_following_text.items():
    #     print(key, value)
    #     bigrams_with_following_text[key].append("ba")
       

            
            
    #print(bigrams_with_following_text.keys()) 
        #pdb.set_trace()
    
    #print(bigrams_with_following_text)
       





    # chains = {}
    # chain_keyes = []
    # # your code goes here
    # words = text_string.split()
    # for word_index in range(len(words)-1):
    #     pdb.set_trace()
    #     #chain_keyes.append((words[word_index], words[word_index + 1]))
    #     words_keys = chains.keys()
    #     chains.get(chain_keyes,0)
    #     # chains.get((words[word_index], words[word_index + 1]), words[word_index + 2])

    #     print(chains)
    #     # print("This is a set of two: {} {}".format(words[word_index],words[word_index+1]))
    #     print(chain_keyes)
    # return chains




def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
