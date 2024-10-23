import os
from word_frequency import count_word_frequencies

def main():
    # Read the input from the input.txt file located in a separate sub-folder
    input_file = os.path.join('input_data', 'input.txt')
    
    with open(input_file, 'r') as f:
        line = f.readline().strip()
    
    # Call the word frequency function
    word_frequencies = count_word_frequencies(line)
    
    # Print the result
    for word, freq in word_frequencies:
        print(f"('{word}', {freq})")

if __name__ == "__main__":
    main()

