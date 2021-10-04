### Task 4.2
# Implement a function which search for most common words in the file.
# Use `data/lorem_ipsum.txt` file as a example.

import collections
import re
import itertools


def most_common_words(filepath, number_of_words=3):

    bank_of_words = []
    counter_dict = collections.Counter()
    with open(filepath, "r") as g:
        list_of_string = g.readlines()
        for string_ in list_of_string:
            bank_of_words.append(re.split(r'[.,\s]', string_))
        bank_of_words = list(itertools.chain(*bank_of_words))
        for word in bank_of_words:
            if word != "":
                counter_dict[word] += 1
        bank_of_words = counter_dict.most_common(number_of_words)
        bank_of_words = list(itertools.chain(*bank_of_words))
        bank_of_words = [c for c in bank_of_words if isinstance(c, str)]
        return bank_of_words


print(most_common_words("lorem_ipsum.txt"))
