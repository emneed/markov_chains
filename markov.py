from random import choice
import sys
import string


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    data_file = open(file_path).read()
    words = data_file.split()

    return words


def make_chains(text_string, num):
    """Takes input text as list; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    #Looping over text_string to build each key
    for index in range(len(text_string) - num):
        keys = ()

        #Fills the key based on number of words in n_gram
        for item in range(num):
            keys = keys + (text_string[index + item],)

        #Assigns the key a value word after the n_gram
        value = text_string[index + num]
        existing_values = chains.get(keys)
        if existing_values is None:
            chains[keys] = [value]
        else:
            existing_values.append(value)
            chains[keys] = existing_values

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    chosen = False

    while not chosen:
        key = choice(chains.keys())
        if key[0][0] in string.ascii_uppercase:
            chosen = True
    text = text + " ".join(key)
    loops = 0

    while True:
    #while len(text) < 140:
        try:
            value = choice(chains[key])
            text += " " + value
            list_key = list(key)[1:]
            key = tuple(list_key) + (value,)
            loops += 1
        except KeyError:
            if text[-1] not in string.punctuation:
                for index, char in enumerate(text[-1::-1]):
                    if (not char.isalpha()) and (char != " "):
                        print index
                        text = text[:(len(text) - index)]
                        return text
            return text
    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(sys.argv[2]))

# Produce random text
random_text = make_text(chains)

print random_text
