from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    data_file = open(file_path).read()
    words = data_file.split()

    return words


def make_chains(text_string):
    """Takes input text as list; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    for index in range(len(text_string) - 2):
        key1 = text_string[index]
        key2 = text_string[index + 1]
        value = text_string[index + 2]
        existing_values = chains.get((key1, key2))
        if existing_values is None:
            chains[(key1, key2)] = [value]
        else:
            existing_values.append(value)
            chains[(key1, key2)] = existing_values

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    key = choice(chains.keys())
    text = key[0] + " " + key[1]

    while True:
        try:
            value = choice(chains[key])
            text += " " + value
            key = (key[1], value)

        except KeyError:
            return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
