import os

def statistics():
    text_file_name = "flie.txt"

    with open(os.path.dirname(__file__) + "/../file.txt", 'r') as file:
        lines = file.readlines()
        
        total_lines = len(lines)
        
        total_words = 0
        for line in lines:
            words = line.split()
            total_words += len(words)
        
        total_chars = 0
        for line in lines:
            total_chars += len(line)
            
    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_chars}")
    print()
