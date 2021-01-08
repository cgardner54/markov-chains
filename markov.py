"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    path = open(file_path)
    text = path.read()
    text = text.replace("\n", " ")
    return text 
    #Contents of your file as one long string'
open_and_read_file('green-eggs.txt')


"""
    Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]

        
        take in the string
        for every two words, make a tuple
        for every tuple, make a list of possible next words
        make a dictionary with tuples as keys, lists as values
    """






    # your code goes here
def make_chains(text_string):
    chains = {}
    words = text_string.split(" ")
    for word in range(len(words)-2):
        key = (words[word], words[word +1])
        value = words[word + 2]
        

        if key not in chains:
            chains[key] = [value]
            #print(chains)
            #print("$$$$$$")
        else:
            chains[key].append(value)
        #print(chains)
        #print("*****") 

    
    return chains

chains = make_chains(open_and_read_file('green-eggs.txt'))

def make_text(chains):
    """Return text from chains."""
    key = choice(list(chains.keys()))
    while key is not ('I', 'am'):
        words = [key[0], key[1]]
        word = choice(chains[key])
        word == key[0]
        append_a_word = words.append(word)
        word = choice(chains[key])
        print(word)
        print("^^^^^")
        break
    
    print("******")
    print(words)
    # print(word)
    # while key is not ('I', 'am'):
    #      word == key[0]
    #      append_a_word = words.append(word)
    #      word = choice(chains[key])
    #      print(append_a_word)
    #      print(word)
    #      print("^^^^^")
    #      break
    # #     
    print(word)
    print("last print")
    #words = [chains[key]]

    # your code goes here

    print(' '.join(words))
    return ' '.join(words)



    #input_path = 'green-eggs.txt'
make_text(chains)

# # Open the file and turn it into one long string
#input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
