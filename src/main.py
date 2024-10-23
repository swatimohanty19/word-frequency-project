import os
from concurrent.futures import ThreadPoolExecutor
from word_frequency import count_word_frequencies

def process_file(file_path):
    with open(file_path, 'r') as f:
        line = f.readline().strip()
    return count_word_frequencies(line)

def main():
    input_file = os.path.join('input_data', 'input.txt')
    
    # Use ThreadPoolExecutor to run the algorithm in parallel
    with ThreadPoolExecutor() as executor:
        future = executor.submit(process_file, input_file)
        word_frequencies = future.result()

    # Print the result
    for word, freq in word_frequencies:
        print(f"('{word}', {freq})")

if __name__ == "__main__":
    main()

