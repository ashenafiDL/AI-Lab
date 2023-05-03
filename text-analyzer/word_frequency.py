
from clean_text import clean_text  # import clean_text
top = 0
# Returns the frequency of words by decreasing order.
def word_frequency():
    print("Enter 0 for all word frequencys ranks or top of you want")
    try: 
        top = int(input("Top of: "))
    except (Exception):
        print("Invalid choice")
        print("Enter 0 for all word frequencys ranks or top of you want")

    """ dictionary = {'word':'amount'}
        'word': stands for all specific words in the list.
        'amount': total amount of the word, for all unique words in the list.
    """
    dictionary = {} 
    
    words = clean_text() #  asign the clean text to the words as a list.

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

    count = 0
    num =0
    print('{:<20} {:<20}'.format("WORDS", "AMOUNT")) # title for displaying the dictionary
    for word, amount in sortedDictionary.items():
        num += 1
        word = str(num)+". "+word
        if top == 0:   # if user choosed 0, always this case will be excuted, means all data will be displayed.
            print('{:<20} {:<20}'.format(word, amount))
        else:
            if count > top-1:  # if user choosed other than 0, words upto his choice will be displayed.
                               # eg. if you entered 5, you will see top 5 frequent word. 
                break
            print('{:<20} {:<20}'.format(word, amount))
            count += 1
    print()

    