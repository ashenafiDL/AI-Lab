from clean_text import clean_text  # import clean_text


def character_frequency():
    """Returns the frequency of characters in the text file and displays the first five most frequently occurring characters."""
    characters = {}
    words = clean_text()

    # count the frequency of each character
    for word in words:
        for char in word:
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    # sort the characters in decreasing order by their frequency
    sorted_characters = dict(sorted(characters.items(), key=lambda x: x[1], reverse=True))

    # display the first five most frequently occurring characters
    print("The first five most frequently occurring characters are:")
    count = 0
    for char, frequency in sorted_characters.items():
        if count > 4:
            break
        print(char, ":", frequency)
        count += 1

    print()
