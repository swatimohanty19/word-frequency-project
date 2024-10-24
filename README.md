# Word Frequency Counter

This project reads a sentence from a file, calculates the word frequency, and displays the result in alphanumeric order.

## Project Structure

- `src/word_frequency.py`: Contains the function to count word frequencies.
- `src/main.py`: The main entry point that reads from the input file and calls the frequency function.
- `tests/test_word_frequency.py`: Contains unit tests for the word frequency function.
- `input_data/input.txt`: The input file containing the text.

## How to Run

1. Clone the repository and navigate to the project folder:

    ```bash
    git clone <repository-url>
    cd word_frequency_project
    ```

2. Run the program:

    ```bash
    python src/main.py
    ```

3. Run the unit tests:

    ```bash
    python -m unittest discover -s tests
    ```


## Multithreading

The word frequency algorithm runs in parallel using Python's `concurrent.futures.ThreadPoolExecutor`.
