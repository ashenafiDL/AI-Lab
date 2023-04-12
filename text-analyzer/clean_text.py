import re


def clean_text():
    """A function to read and clean a text file - removes all special characters,
    :return: A list of words
    """
    words = []
    with open("../file.txt", "r") as f:
        for line in f:
            for word in line.split():
                word = re.sub(r"\W", "", word)  # remove non-alphanumeric characters
                word = re.sub(r"\d", "", word)  # remove numeric characters
                words.append(word.lower())
    return words
