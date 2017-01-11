import markov
import sys

characters = {"Lane.": [], "Algernon.": [], "Jack.": [], "Gwendolen.": [],
              "Lady": [], "Miss": []}


def read_file_by_line(file_name):

    data_file = open(file_name)
    for line in data_file:
        line = line.strip()
        tokens = line.split()
        if len(tokens) > 1:
            name = tokens[0]
            if name in characters.keys():
                existing_values = characters[name]
                if len(existing_values) == 0:
                    characters[name] = tokens[1:]
                else:
                    existing_values.extend(tokens[1:])
                    characters[name] = existing_values

    data_file.close()


read_file_by_line(sys.argv[1])

num = int(sys.argv[2])

lane_chains = markov.make_chains(characters["Lane."], num)
algernon_chains = markov.make_chains(characters["Algernon."], num)
jack_chains = markov.make_chains(characters["Jack."], num)
lady_chains = markov.make_chains(characters["Lady"], num)
miss_chains = markov.make_chains(characters["Miss"], num)

print markov.make_text(algernon_chains)
