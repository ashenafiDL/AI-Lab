import os
from clean_text import clean_text

def statistics(): 
    total_lines, total_words, total_chars = 0, 0, 0
    file = open(os.path.dirname(__file__) + "/../file.txt", mode="r", encoding="utf-8")
    for line in file: 
        total_lines += 1 
            
    words = clean_text() 
    total_words = len(words)

    for word in words:
        total_chars += len(word)

    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_chars}")
    print() 
