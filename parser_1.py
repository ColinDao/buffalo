import nltk
import sys
import re
from nltk.tree import Tree

# Context-free grammar (CFG) end states
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# CFG non-end states
NONTERMINALS = """
S -> NP VP
NP -> N | C N
C -> P | P D | D
D -> Det | Det A
A -> Adj | Adj A
VP -> V | Adv | Adv VP | Conj VP | V VP | V NP | VP NP | NP VP
"""

# Create CFG rules
grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)

# Create parser based on CFG rules
parser = nltk.ChartParser(grammar)


def main():

    # Download tokenizer model
    nltk.download("punkt")

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    return [word for word in nltk.word_tokenize(sentence.lower()) if re.search("[a-z]", word)]


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    # List for subtrees with a label of "NP"
    np_list = []

    # Depth-first search (DFS) on current tree
    def dfs(tree):

        # Found a subtree with label "NP"
        if tree.label() == "NP":
            np_list.append(tree)
        else:

            # Search through lower level subtrees
            for subtree in tree:

                # Not at a leaf
                if isinstance(subtree, Tree):
                    dfs(subtree)
    
    # Perform DFS on given tree
    dfs(tree)

    return np_list


if __name__ == "__main__":
    main()
