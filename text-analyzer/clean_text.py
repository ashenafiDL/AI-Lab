import re
import os


def clean_text():
    """A function to read and clean a text file - removes all special characters,
    :return: A list of words
    """
    words = []
    with open(os.path.dirname(__file__) + "/../file.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                # remove non-alphanumeric characters
                word = re.sub(r"\W", "", word)
                word = re.sub(r"\d", "", word)  # remove numeric characters
                words.append(word.lower())
    return words
