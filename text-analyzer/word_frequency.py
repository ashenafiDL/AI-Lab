from clean_text import clean_text
words = clean_text()
def word_frequency():

    '''
        dictionary = {'word':'amount'}
        'word': stands for all specific words in the list.
        'amount': total amount of the word, for all unique words in the list.
    '''
    dictionary = {} 

    # take one word per iteration
    for word in words:
        if word not in dictionary:
            # if the word is not added in the dictionary then newly add to the dictionary and value set to 1.
            dictionary[word] = 1
        else:
            # if the word is present in dictionary, then increment the amount by one for this specific word only. 
            dictionary[word] += 1 


    # sort the words in decreasing order by their amout.
    sortedDictionary = dict(sorted(dictionary.items(), key=lambda w: w[1], reverse=True))

    for word, key in sortedDictionary.items():
        print(word,key)

 