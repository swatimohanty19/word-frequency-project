def count_word_frequencies(line):
    # Split the input line into words
    words = line.split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Sort the dictionary by keys (words) alphanumerically
    sorted_word_freq = sorted(word_freq.items())
    return sorted_word_freq

